import pandas as pd
from rest_framework import viewsets, status
from rest_framework.response import Response
from employee.serializers import CompanySerializer, EmployeeSerializer
from employee.models import Company


class AddDataViewSet(viewsets.ViewSet):
    def create(self, request):
        try:
            # read excel file using pandas and convert column names to lower case
            data = pd.read_excel("Practical Task Python sheet.xlsx", engine="openpyxl")
            data.columns = data.columns.str.lower()

            # get unique company names and pass it into serializer
            companies = data["company_name"].unique()
            company_serializer = CompanySerializer(data={"companies": companies})
            company_serializer.is_valid(raise_exception=True)
            company_list = company_serializer.validated_data["companies"]

            # check if company name is already present in table to avoid adding same name
            existing_companies = Company.objects.filter(company_name__in=company_list).values_list("company_name",
                                                                                                   flat=True)
            # create company objects
            companies_to_create = [Company(company_name=company) for company in company_list if
                                   company not in existing_companies]
            # add companies in bulk to table
            Company.objects.bulk_create(companies_to_create)

            # get employees data
            employee_data = data[
                ['employee_id', 'first_name', 'last_name', 'phone_number', 'salary', 'manager_id', 'department_id',
                 'company_name']
            ]

            # ------- logic to replace company name in employee_data with company id --------
            # Fetch company name to ID mapping from the Company model
            company_df = pd.DataFrame(list(Company.objects.all().values('id', 'company_name')))
            # Merge employee_data with company_df based on company name
            merged_df = employee_data.merge(company_df, how='left', left_on='company_name', right_on='company_name')

            # Drop the 'company_name' column and rename 'id' to 'company'
            merged_df.drop(['company_name', 'company_name'], axis=1, inplace=True)
            merged_df.rename(columns={'id': 'company'}, inplace=True)
            # Convert merged DataFrame back to a list of dictionaries
            employee_data_with_ids = merged_df.to_dict(orient="records")

            # pass data in serializer and save all records only if serializer is valid i.e if records are not already present
            employee_serializer = EmployeeSerializer(data=employee_data_with_ids, many=True)
            if employee_serializer.is_valid():
                employee_serializer.save()
                message = "Data successfully added in the table"
                res_status = True
                res_code = status.HTTP_200_OK
            else:
                message = "Data already added in table. Please check database"
                res_status = False
                res_code = status.HTTP_400_BAD_REQUEST
        except Exception as error:
            message = str(error)
            res_status = False
            res_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        response = {
            "data": None,
            "message": message,
            "status": res_status,
            "code": res_code
        }
        return Response(response, res_code)
