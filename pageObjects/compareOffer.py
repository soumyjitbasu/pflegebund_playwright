import json
from playwright.sync_api import Page, expect
import time



class CompareOffer:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        with open('data/credentials.json') as f:
            test_data = json.load(f)
            baseURL = test_data["baseURL"]
        self.page.goto(baseURL)


    def e2eFlow(self, noOfPerson, verificationAdditionalPerson, additionalPersonOption, verificationMobilePage, mobilePageOption, verificationNightShift, nightShiftOption, verificationCaregiverDrive, caregiverDriveOption, verificationGermanProficiency, germanProficiencyOption, verificationNursingStaffGender, nursingStaffGenderOption, verificationWhenCareNeeded, whenCareNeededOption, verificationWhereCareNeeded, whereCareNeededPlace, verificationContactInformation, contactInformationName, contactInformationEmail, contactInformationNumber ):
        self.page.get_by_text(noOfPerson).click()
        print(verificationAdditionalPerson)
        time.sleep(3)
        expect(self.page.locator("body")).to_contain_text("Befindet sich eine zusätzliche Person (ohne Pflegebedarf) mit im Haushalt?")

        # Clicking on the yes button.
        self.page.get_by_role("button", name=additionalPersonOption).click()
        time.sleep(3)
        expect(self.page.locator("body")).to_contain_text("Wie mobil ist die zu pflegende Person?")


        # clicking the mobile option
        self.page.get_by_role("button", name=mobilePageOption).click()
        time.sleep(3)
        expect(self.page.locator("body")).to_contain_text("Sind Nachteinsätze nötig?")


        # clicking the No option on Are Night Shift Necessary page
        self.page.get_by_role("button", name=nightShiftOption).click()
        time.sleep(3)
        expect(self.page.locator("body")).to_contain_text("Muss die Pflegekraft Auto fahren?")


        # Clicking on the Yes button on the Does Care Giver have to Drive page
        self.page.get_by_role("button", name=caregiverDriveOption).click()
        time.sleep(3)
        expect(self.page.locator("body")).to_contain_text("Welche Deutschkenntnisse wünschen Sie?")


        # clicking on Advanced button on What level of German do you want page
        self.page.get_by_role("button", name=germanProficiencyOption).click()
        time.sleep(3)
        expect(self.page.locator("body")).to_contain_text("Wünschen Sie eine weibliche oder männliche Pflegehilfe?")

        # Choosing Female on Do you want male / female nurshing staff
        self.page.get_by_role("button", name=nursingStaffGenderOption).click()
        time.sleep(3)
        expect(self.page.locator("body")).to_contain_text("Wann wird die Betreuung benötigt?")


        # Choosing Still unclear on When is care needed page
        self.page.get_by_role("button", name=whenCareNeededOption).click()
        time.sleep(3)
        expect(self.page.locator("body")).to_contain_text("Wo wird die Betreuung benötigt?")


        # Entering value where is care needed page
        self.page.locator("#city").fill(whereCareNeededPlace)
        self.page.get_by_role("button", name="Weiter").click()
        time.sleep(3)
        expect(self.page.locator("body")).to_contain_text("Wer soll unser Ansprechpartner für die Angebote sein?")

        # Entering name, email and phone number in the last page and completing the flow
        self.page.get_by_placeholder("Ihr vollständiger Name").fill(contactInformationName)
        self.page.get_by_placeholder("E-Mail").fill(contactInformationEmail)
        self.page.get_by_placeholder("Ihre Telefonnummer").fill(contactInformationNumber)
        self.page.get_by_role("checkbox").check()
        self.page.get_by_role("button", name="Jetzt Angebote vergleichen").click()
        expect(self.page.locator("body")).to_contain_text(" Vielen Dank für Ihre Anfrage! ")


