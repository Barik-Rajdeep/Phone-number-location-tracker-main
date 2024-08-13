import json
import phonenumbers
import pycountry
from tkinter import Tk, Label, Button, Entry
from phonenumbers import carrier
from phonenumbers import geocoder
from phone_iso3166.country import phone_country
from geopy.geocoders import Nominatim

class Track:
    def __init__(self, App):    
        
        self.window = App
        self.window.title("Phone number Tracker")
        self.window.geometry("500x400")
        self.window.configure(bg="#2f2212")
        
        self.window.resizable(True, True)    
        Label(App, text="Enter the phone number", fg="orange", font=("Times", 20), bg="#3f5edb").place(x=150, y=30)
        self.mobile_number = Entry(App, width=14, font=("Arial", 15), relief="flat")
        self.trackingbutton = Button(App, text="To track the number click here", bg="#22c6c3", relief="sunken")
        self.countryname = Label(App, fg="white", font=("Times", 20), bg="#3f5efb")
        self.countryname2 = Label(App, fg="white", font=("Times", 20), bg="#3f5efb")
        self.location_coords = Label(App, fg="white", font=("Times", 20), bg="#3f5efb")
        self.mobile_number.place(x=170, y=120)
        self.trackingbutton.place(x=200, y=200)
        self.countryname.place(x=100, y=280)     
        
        self.countryname2.place(x=300, y=280)
        self.location_coords.place(x=100, y=320)
        self.trackingbutton.bind("<Button-1>", self.Track_THE_location)           

    def Track_THE_location(self, event):    
        phone_number = self.mobile_number.get()
        if phone_number:
            try:
                tracked = phonenumbers.parse(phone_number)
                
                self.countryname.configure(text=carrier.name_for_number(tracked, "en"))
                country = geocoder.description_for_number(tracked, "en")
                self.countryname2.configure(text=country)
                
                # Find latitude and longitude
                geolocator = Nominatim(user_agent="phone_tracker")
                location = geolocator.geocode(country)
                if location:
                    lat = location.latitude
                    lon = location.longitude
                    lat_dir = "N" if lat >= 0 else "S"
                    lon_dir = "E" if lon >= 0 else "W"
                    self.location_coords.configure(text=f"Lat: {abs(lat):.4f}°{lat_dir}, Long: {abs(lon):.4f}°{lon_dir}")
                else:
                    self.location_coords.configure(text="Coordinates not found")
            except phonenumbers.phonenumberutil.NumberParseException:
                self.countryname.configure(text="Invalid number")
                self.countryname2.configure(text="")
                self.location_coords.configure(text="")

PhoneTracking = Tk()
MyApp = Track(PhoneTracking)

PhoneTracking.mainloop()
