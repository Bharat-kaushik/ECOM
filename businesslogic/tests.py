from django.test import TestCase
from datetime import datetime

from userPlus.models import Company
from userPlus.models import Country
from businesslogic.domain.exam_schedule import ExamSchedule
from businesslogic.repositories.company_repository import CompanyRepository
from businesslogic.services.company_service import add_company


class CompanyTestCases(TestCase):

    def setUp(self):
        Country.objects.create(Name="India")
        Country.objects.create(Name="UK")

        country = Country.objects.get(Name="India")

        add_company(company_name="Company Name 1",
                    legal_name="Legal Name 1",
                    pan_card="Pan Card 1",
                    tax_id="ABC XTTU",
                    username="UserName1",
                    mobile="1234567890",
                    address1="Address line 1",
                    address2="Address Line2",
                    locality="Locality",
                    city="Noida",
                    state="UP",
                    country=country,
                    postal_code="201301")
        Company.objects.create(CompanyKey="CompKey2",
                               CompanyName="Company Name 2",
                               LegalName="Legal Name 2",
                               PANCard="Pan Card 2",
                               TaxID="ABC XTTU",
                               Username="UserName2",
                               Mobile="1234567890",
                               AddressLine1="Address line 1",
                               AddressLine2="Address Line2",
                               Locality="Locality",
                               City="Noida",
                               State="UP",
                               Country=country,
                               PostalCode="201301",
                               CreatedOn=datetime.utcnow(),
                               UpdatedOn=datetime.utcnow()
                               )

    def test_company_name(self):
        comp = Company.objects.first()
        company = Company.objects.get(pk=comp.Id)
        self.assertEqual(company.CompanyName, "Company Name 1")

    def test_company_by_company_key(self):
        comp_repo = CompanyRepository()
        company = comp_repo.get_company_by_company_key("CompKey2")
        self.assertEquals(company.CompanyName, "Company Name 2")

    def test_company_by_pk(self):
        comp = Company.objects.first()
        comp_repo = CompanyRepository()
        company = comp_repo.get_by_pk(comp.Id)
        self.assertEquals(company.Id, comp.Id)

    def test_company_save(self):
        country = Country.objects.get(Name="India")
        company = add_company(company_name="Company Name 3",
                              legal_name="Legal Name 3",
                              pan_card="Pan Card 3",
                              tax_id="ABC XTTU3",
                              username="UserName3",
                              mobile="1234567890",
                              address1="Address line 1",
                              address2="Address Line2",
                              locality="Locality",
                              city="Noida",
                              state="UP",
                              country=country,
                              postal_code="201301")

        self.assertIsNotNone(company)
        self.assertGreater(company.Id, 0, "Company id must not be zero or negative")

    def test_company_update(self):
        comp_repo = CompanyRepository()
        company = comp_repo.get_company_by_company_key("CompKey2")
        self.assertEquals(company.CompanyName, "Company Name 2")

        company.CompanyName = "Updated Name"
        comp_repo.update(company)
        company = comp_repo.get_company_by_company_key("CompKey2")
        self.assertEquals(company.CompanyName, "Updated Name")
