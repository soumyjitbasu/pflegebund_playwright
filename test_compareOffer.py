import time
import pytest
from playwright.sync_api import Playwright
import json

from tomlkit.items import String

from pageObjects.compareOffer import CompareOffer

with open('data/e2eflow.json') as f:
    e2e_data = json.load(f)
    e2e_data_list = e2e_data['e2e']
    print(e2e_data_list)
@pytest.mark.parametrize('e2e_data', e2e_data_list)
def test_compareOffer(playwright: Playwright, e2e_data):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()


    #Getting the data from the json file
    noOfPerson = e2e_data["noOfPerson"]
    verificationAdditionalPerson = e2e_data["verificationAdditionalPerson"]
    additionalPersonOption = e2e_data["additionalPersonOption"]
    verificationMobilePage = e2e_data["verificationMobilePage"]
    mobilePageOption = e2e_data["mobilePageOption"]
    verificationNightShift = e2e_data["verificationNightShift"]
    nightShiftOption = e2e_data["nightShiftOption"]
    verificationCaregiverDrive = e2e_data["verificationCaregiverDrive"]
    caregiverDriveOption = e2e_data["caregiverDriveOption"]
    verificationGermanProficiency = e2e_data["verificationGermanProficiency"]
    germanProficiencyOption = e2e_data["germanProficiencyOption"]
    verificationNursingStaffGender = e2e_data["verificationNursingStaffGender"]
    nursingStaffGenderOption = e2e_data["nursingStaffGenderOption"]
    verificationWhenCareNeeded = e2e_data["verificationWhenCareNeeded"]
    whenCareNeededOption = e2e_data["whenCareNeededOption"]
    verificationWhereCareNeeded = e2e_data["verificationWhereCareNeeded"]
    whereCareNeededPlace = e2e_data["whereCareNeededPlace"]
    verificationContactInformation = e2e_data["verificationContactInformation"]
    contactInformationName = e2e_data["contactInformationName"]
    contactInformationEmail = e2e_data["contactInformationEmail"]
    contactInformationNumber = e2e_data["contactInformationNumber"]

    compareOffer = CompareOffer(page)
    compareOffer.navigate()
    compareOffer.e2eFlow(noOfPerson, verificationAdditionalPerson, additionalPersonOption, verificationMobilePage, mobilePageOption, verificationNightShift, nightShiftOption, verificationCaregiverDrive, caregiverDriveOption, verificationGermanProficiency, germanProficiencyOption, verificationNursingStaffGender, nursingStaffGenderOption, verificationWhenCareNeeded, whenCareNeededOption, verificationWhereCareNeeded, whereCareNeededPlace, verificationContactInformation, contactInformationName, contactInformationEmail, contactInformationNumber)