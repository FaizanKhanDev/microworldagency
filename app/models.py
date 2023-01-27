from django.db import models

class Favicon(models.Model):
    img = models.ImageField(upload_to='images')

class Headeritem(models.Model):
    PhoneNumber = models.CharField(max_length=40)
    PhoneNumberUrl = models.CharField(max_length=40)
    Email = models.CharField(max_length=40)
 
class NavLogo(models.Model):
    logo = models.CharField(max_length=20)


class Hometitle(models.Model):
    title1 = models.CharField(max_length=20)
    title2 = models.CharField(max_length=20)
    title3 = models.CharField(max_length=20)
    description1 = models.TextField(max_length=200)
    description2 = models.TextField(max_length=200)

class HomeIcons(models.Model):
    icon1 = models.ImageField(upload_to='images')
    icon2 = models.ImageField(upload_to='images')
    icon3 = models.ImageField(upload_to='images')
    icon4 = models.ImageField(upload_to='images')

class ContactIcons(models.Model):
    icon1 = models.ImageField(upload_to='images')
    icon2 = models.ImageField(upload_to='images')
    icon3 = models.ImageField(upload_to='images')

class Homeservicestitle(models.Model):
    title = models.CharField(max_length=100)
    subtitle1 = models.CharField(max_length=50)
    description1 = models.TextField(max_length=200)
    subtitle2 = models.CharField(max_length=50)
    description2 = models.TextField(max_length=200)
    subtitle3 = models.CharField(max_length=50)
    description3 = models.TextField(max_length=200)


class Homesectionthird(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=600)
    img = models.ImageField(upload_to='images')
    subtitle1 = models.CharField(max_length=50)
    subdescription1 = models.TextField(max_length=200)
    subtitle2 = models.CharField(max_length=50)
    subdescription2 = models.TextField(max_length=200)


class Homesectionfour(models.Model):
    img = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100)
    meter1 = models.CharField(max_length=100)
    subtitle1 = models.CharField(max_length=50)
    subdescription1 = models.TextField(max_length=200)
    meter2 = models.CharField(max_length=100)
    subtitle2 = models.CharField(max_length=50)
    subdescription2 = models.TextField(max_length=200)



class Homesectionfifth(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=600)
    img = models.ImageField(upload_to='images')
    subtitle1 = models.CharField(max_length=50)
    subdescription1 = models.TextField(max_length=200)
    subtitle2 = models.CharField(max_length=50)
    subdescription2 = models.TextField(max_length=200)



class Homesectionsixth(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
   

class HomeBlog(models.Model):
    img = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100)


class HomeletDiscus(models.Model):
    title = models.CharField(max_length=200)



# ===== About PAge ====  #
class AboutBg(models.Model):
    img = models.ImageField(upload_to='images')
    video = models.CharField(max_length=600)


class AboutTitle(models.Model):
    title = models.CharField(max_length=100)

class AboutSectionTwo(models.Model):
    title = models.CharField(max_length=100)
    description1 = models.TextField(max_length=600)
    description2 = models.TextField(max_length=600)

class AboutSectionthree(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images')

class AboutSkill(models.Model):
    skill = models.TextField(max_length=100)
    percentage = models.TextField(max_length=100)



class AboutSectionfour(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=600)
    subtitle1 = models.CharField(max_length=50)
    description1 = models.TextField(max_length=200)
    subtitle2 = models.CharField(max_length=50)
    description2 = models.TextField(max_length=200)
    subtitle3 = models.CharField(max_length=50)
    description3 = models.TextField(max_length=200)
    subtitle4 = models.CharField(max_length=50)
    description4 = models.TextField(max_length=200)


class AboutSectionfifth(models.Model):
    img = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100)
    meter1 = models.CharField(max_length=100)
    subtitle1 = models.CharField(max_length=50)
    subdescription1 = models.TextField(max_length=200)
    meter2 = models.CharField(max_length=100)
    subtitle2 = models.CharField(max_length=50)
    subdescription2 = models.TextField(max_length=200)


class AboutSectionSixth(models.Model):
    title = models.CharField(max_length=200)
# ===== About Page ====  #



# ===== services Page ====  #

class ServicesBg(models.Model):
    img = models.ImageField(upload_to='images')
    video = models.CharField(max_length=600)



class ServicesTitle(models.Model):
    title  = models.CharField(max_length=100)


class ServicessectionTwo(models.Model):
    title = models.CharField(max_length=100)
    description1 = models.TextField(max_length=600)
    description2 = models.TextField(max_length=600)

class ServicesCategorie(models.Model):
    title1 = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
    title3 = models.CharField(max_length=100)
    title4 = models.CharField(max_length=100)
    title5 = models.CharField(max_length=100)
    title6 = models.CharField(max_length=100)


class Servicessectionthree(models.Model):
    img  = models.ImageField(upload_to='images')
   
class ServicessectionSubthree(models.Model):
    title1 = models.CharField(max_length=100)
    description1 = models.CharField(max_length=600)
    title2 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=600)
    title3 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=600)


class Servicessectionfour(models.Model):
    img  = models.ImageField(upload_to='images')
   
class ServicessectionSubfour(models.Model):
    title1 = models.CharField(max_length=100)
    description1 = models.CharField(max_length=600)
    title2 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=600)
    title3 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=600)

class Servicessectionfifth(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=600)

class ContactPhoneAndEmail(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=100)
    PhoneNumberUrl = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class ContactImg(models.Model):
    img = models.ImageField(upload_to='images')
class Servicessectionsixth(models.Model):
    title = models.CharField(max_length=100)



# ===== services Page ====  #
# === Content Wrinting == #

class ContentServicesBg(models.Model):
    img = models.ImageField(upload_to='images')
    video = models.CharField(max_length=600)



class ContentServicesTitle(models.Model):
    title  = models.CharField(max_length=100)


class ContentServicessectionTwo(models.Model):
    title = models.CharField(max_length=100)
    description1 = models.TextField(max_length=600)
    description2 = models.TextField(max_length=600)

class ContentServicesCategorie(models.Model):
    title1 = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
    title3 = models.CharField(max_length=100)
    title4 = models.CharField(max_length=100)
    title5 = models.CharField(max_length=100)
    title6 = models.CharField(max_length=100)
    title7 = models.CharField(max_length=100, null=True, blank=True)
    title8 = models.CharField(max_length=100, null=True, blank=True)
    title9 = models.CharField(max_length=100, null=True, blank=True)

class ContentWritingAllIcons(models.Model):
    icon1 = models.ImageField(upload_to='images')
    icon2 = models.ImageField(upload_to='images')
    icon3 = models.ImageField(upload_to='images')
    icon4 = models.ImageField(upload_to='images')
    icon5 = models.ImageField(upload_to='images')
    icon6 = models.ImageField(upload_to='images')
    icon7 = models.ImageField(upload_to='images', null=True, blank=True)
    icon8 = models.ImageField(upload_to='images', null=True, blank=True)
    icon9 = models.ImageField(upload_to='images', null=True, blank=True)

class ContentServicessectionthree(models.Model):
    img  = models.ImageField(upload_to='images')
   
class ContentServicessectionSubthree(models.Model):
    title1 = models.CharField(max_length=100)
    description1 = models.CharField(max_length=600)
    title2 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=600)
    title3 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=600)


class ContentServicessectionfour(models.Model):
    img  = models.ImageField(upload_to='images')
   
class ContentServicessectionfive(models.Model):
    img  = models.ImageField(upload_to='images')

class ContentServicessectionSubfour(models.Model):
    title1 = models.CharField(max_length=100)
    description1 = models.CharField(max_length=600)
    title2 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=600)
    title3 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=600)

class ContentServicessectionSubfive(models.Model):
    title1 = models.CharField(max_length=100)
    description1 = models.CharField(max_length=600)
    title2 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=600)
    title3 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=600)


class ContentServicessectionfifth(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=600)


class ContentServicessectionsixth(models.Model):
    title = models.CharField(max_length=100)


# === Content Wrinting == #

# === video Editing == #

class VideoEditingBg(models.Model):
    img = models.ImageField(upload_to='images')
    video = models.CharField(max_length=600)



class VideoEditingTitle(models.Model):
    title  = models.CharField(max_length=100)


class VideoEditingsectionTwo(models.Model):
    title = models.CharField(max_length=100)
    description1 = models.TextField(max_length=600)
    description2 = models.TextField(max_length=600)

class VideoEditingCategorie(models.Model):
    title1 = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
    title3 = models.CharField(max_length=100)
    title4 = models.CharField(max_length=100)
    title5 = models.CharField(max_length=100)
    title6 = models.CharField(max_length=100)
    title7 = models.CharField(max_length=100, null=True, blank=True)
    title8 = models.CharField(max_length=100, null=True, blank=True)
    title9 = models.CharField(max_length=100, null=True, blank=True)
    title10 = models.CharField(max_length=100, null=True, blank=True)
    title11 = models.CharField(max_length=100, null=True, blank=True)
    title12 = models.CharField(max_length=100, null=True, blank=True)


class VideoEditingAllIcons(models.Model):
    icon1 = models.ImageField(upload_to='images')
    icon2 = models.ImageField(upload_to='images')
    icon3 = models.ImageField(upload_to='images')
    icon4 = models.ImageField(upload_to='images')
    icon5 = models.ImageField(upload_to='images')
    icon6 = models.ImageField(upload_to='images')
    icon7 = models.ImageField(upload_to='images')
    icon8 = models.ImageField(upload_to='images')
    icon9 = models.ImageField(upload_to='images')
    icon10 = models.ImageField(upload_to='images')
    icon11 = models.ImageField(upload_to='images')
    icon12 = models.ImageField(upload_to='images')


class VideoEditingsectionthree(models.Model):
    img  = models.ImageField(upload_to='images')
   
class VideoEditingsectionSubthree(models.Model):
    title1 = models.CharField(max_length=100)
    description1 = models.CharField(max_length=600)
    title2 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=600)
    title3 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=600)


class VideoEditingsectionfour(models.Model):
    img  = models.ImageField(upload_to='images')
   
class VideoEditingsectionSubfour(models.Model):
    title1 = models.CharField(max_length=100)
    description1 = models.CharField(max_length=600)
    title2 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=600)
    title3 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=600)


class VideoEditingsectionfive(models.Model):
    img  = models.ImageField(upload_to='images')
   
class VideoEditingsectionSubfive(models.Model):
    title1 = models.CharField(max_length=100)
    description1 = models.CharField(max_length=600)
    title2 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=600)
    title3 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=600)


class VideoEditingSixth(models.Model):
    img  = models.ImageField(upload_to='images')
   
class VideoEditingSubSixth(models.Model):
    title1 = models.CharField(max_length=100)
    description1 = models.CharField(max_length=600)
    title2 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=600)
    title3 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=600)


class VideoEditingsectionfifth(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=600)


class VideoEditingsectionsixth(models.Model):
    title = models.CharField(max_length=100)

# === video Editing == #
# === DigitalMArketing ===  #
class DigitalMarketingBg(models.Model):
    img = models.ImageField(upload_to='images')
    video = models.CharField(max_length=600)



class DigitalMarketingTitle(models.Model):
    title  = models.CharField(max_length=100)


class DigitalMarketingsectionTwo(models.Model):
    title = models.CharField(max_length=100)
    description1 = models.TextField(max_length=600)
    description2 = models.TextField(max_length=600)

class DigitalMarketingCategorie(models.Model):
    title1 = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
    title3 = models.CharField(max_length=100)
    title4 = models.CharField(max_length=100)
    title5 = models.CharField(max_length=100)
    title6 = models.CharField(max_length=100)

class DigitalMarketingAllIcons(models.Model):
    icon1 = models.ImageField(upload_to='images')
    icon2 = models.ImageField(upload_to='images')
    icon3 = models.ImageField(upload_to='images')
    icon4 = models.ImageField(upload_to='images')
    icon5 = models.ImageField(upload_to='images')
    icon6 = models.ImageField(upload_to='images')

class DigitalMarketingsectionthree(models.Model):
    img  = models.ImageField(upload_to='images')
   
class DigitalMarketingSubthree(models.Model):
    title1 = models.CharField(max_length=100)
    description1 = models.CharField(max_length=600)
    title2 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=600)
    title3 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=600)


class DigitalMarketingsectionfour(models.Model):
    img  = models.ImageField(upload_to='images')
   
class DigitalMarketingSubfour(models.Model):
    title1 = models.CharField(max_length=100)
    description1 = models.CharField(max_length=600)
    title2 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=600)
    title3 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=600)

class DigitalMarketingsectionfifth(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=600)


class DigitalMarketingsectionsixth(models.Model):
    title = models.CharField(max_length=100)

# === DigitalMArketing ===  #
# === SEOSEM ===  #

class SEOSEMBg(models.Model):
    img = models.ImageField(upload_to='images')
    video = models.CharField(max_length=600)



class SEOSEMTitle(models.Model):
    title  = models.CharField(max_length=100)


class SEOSEMsectionTwo(models.Model):
    title = models.CharField(max_length=100)
    description1 = models.TextField(max_length=600)
    description2 = models.TextField(max_length=600)

class SEOSEMCategorie(models.Model):
    title1 = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
    title3 = models.CharField(max_length=100)
    title4 = models.CharField(max_length=100)
    title5 = models.CharField(max_length=100)
    title6 = models.CharField(max_length=100)
    title7 = models.CharField(max_length=100, null=True, blank=True)
    title8 = models.CharField(max_length=100, null=True, blank=True)
    title9 = models.CharField(max_length=100, null=True, blank=True)


class SeoSemAllIcons(models.Model):
    icon1 = models.ImageField(upload_to='images')
    icon2 = models.ImageField(upload_to='images')
    icon3 = models.ImageField(upload_to='images')
    icon4 = models.ImageField(upload_to='images')
    icon5 = models.ImageField(upload_to='images')
    icon6 = models.ImageField(upload_to='images')
    icon7 = models.ImageField(upload_to='images')
    icon8 = models.ImageField(upload_to='images')
    icon9 = models.ImageField(upload_to='images')

class SEOSEMSectionFive(models.Model):
    img  = models.ImageField(upload_to='images')


   
class SEOSEMSubtFive(models.Model):
    title1 = models.CharField(max_length=100)
    description1 = models.CharField(max_length=600)
    title2 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=600)
    title3 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=600)

class SEOSEMsectionthree(models.Model):
    img  = models.ImageField(upload_to='images')
   
class SEOSEMSubthree(models.Model):
    title1 = models.CharField(max_length=100)
    description1 = models.CharField(max_length=600)
    title2 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=600)
    title3 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=600)


class SEOSEMsectionfour(models.Model):
    img  = models.ImageField(upload_to='images')
   
class SEOSEMSubfour(models.Model):
    title1 = models.CharField(max_length=100)
    description1 = models.CharField(max_length=600)
    title2 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=600)
    title3 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=600)

class SEOSEMsectionfifth(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=600)


class SEOSEMsectionsixth(models.Model):
    title = models.CharField(max_length=100)

# === SEOSEM ===  #
# === Web services page ==== #

class WebServicesBg(models.Model):
    img = models.ImageField(upload_to='images')
    video = models.CharField(max_length=600)



class WebServicesTitle(models.Model):
    title  = models.CharField(max_length=100)


class WebServicessectionTwo(models.Model):
    title = models.CharField(max_length=100)
    description1 = models.TextField(max_length=600)
    description2 = models.TextField(max_length=600)

class WebServicesCategorie(models.Model):
    title1 = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
    title3 = models.CharField(max_length=100)
    title4 = models.CharField(max_length=100)
    title5 = models.CharField(max_length=100)
    title6 = models.CharField(max_length=100)

class WebAllIcons(models.Model):
    icon1 = models.ImageField(upload_to='images')
    icon2 = models.ImageField(upload_to='images')
    icon3 = models.ImageField(upload_to='images')
    icon4 = models.ImageField(upload_to='images')
    icon5 = models.ImageField(upload_to='images')
    icon6 = models.ImageField(upload_to='images')


class WebServicessectionthree(models.Model):
    img  = models.ImageField(upload_to='images')
   
class WebServicessectionSubthree(models.Model):
    title1 = models.CharField(max_length=100)
    description1 = models.CharField(max_length=600)
    title2 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=600)
    title3 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=600)


class WebServicessectionfour(models.Model):
    img  = models.ImageField(upload_to='images')
   
class WebServicessectionSubfour(models.Model):
    title1 = models.CharField(max_length=100)
    description1 = models.CharField(max_length=600)
    title2 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=600)
    title3 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=600)

class WebServicessectionfifth(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=600)

class WebServicessectionsixth(models.Model):
    title = models.CharField(max_length=100)

# === Web Services Page  ==== #
# === Graphics ==== #

class GraphicsServicesBg(models.Model):
    img = models.ImageField(upload_to='images')
    video = models.CharField(max_length=600)



class GraphicsServicesTitle(models.Model):
    title  = models.CharField(max_length=100)


class GraphicsServicessectionTwo(models.Model):
    title = models.CharField(max_length=100)
    description1 = models.TextField(max_length=600)
    description2 = models.TextField(max_length=600)

class GraphicsServicesCategorie(models.Model):
    title1 = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
    title3 = models.CharField(max_length=100)
    title4 = models.CharField(max_length=100)
    title5 = models.CharField(max_length=100)
    title6 = models.CharField(max_length=100)
    title7 = models.CharField(max_length=100)
    title8 = models.CharField(max_length=100)
    title9 = models.CharField(max_length=100)

class GraphicsAllIcons(models.Model):
    icon1 = models.ImageField(upload_to='images')
    icon2 = models.ImageField(upload_to='images')
    icon3 = models.ImageField(upload_to='images')
    icon4 = models.ImageField(upload_to='images')
    icon5 = models.ImageField(upload_to='images')
    icon6 = models.ImageField(upload_to='images')
    icon7 = models.ImageField(upload_to='images')
    icon8 = models.ImageField(upload_to='images')
    icon9 = models.ImageField(upload_to='images')


class GraphicsServicessectionthree(models.Model):
    img  = models.ImageField(upload_to='images')
   
class GraphicsServicessectionSubthree(models.Model):
    title1 = models.CharField(max_length=100)
    description1 = models.CharField(max_length=600)
    title2 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=600)
    title3 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=600)


class GraphicsServicessectionfour(models.Model):
    img  = models.ImageField(upload_to='images')
   


class GraphicsServicessectionSubfour(models.Model):
    title1 = models.CharField(max_length=100)
    description1 = models.CharField(max_length=600)
    title2 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=600)
    title3 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=600)

class Graphicsfive(models.Model):
    img  = models.ImageField(upload_to='images')

class GraphicsSubfive(models.Model):
    title1 = models.CharField(max_length=100)
    description1 = models.CharField(max_length=600)
    title2 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=600)
    title3 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=600)



class GraphicsServicessectionfifth(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=600)

class GraphicsContact(models.Model):
    img = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)

class GraphicsContactDetail(models.Model):
    PhoneNumber = models.CharField(max_length=100)
    PhoneUrl = models.CharField(max_length=100)
    email = models.TextField(max_length=100)

class GraphicsServicessectionsixth(models.Model):
    title = models.CharField(max_length=100)


# ===== Graphics Page ====  #
# ===== Contact Page ====  #
class ContactBg(models.Model):
    img = models.ImageField(upload_to='images')
    video = models.CharField(max_length=600)
    
class Contacttitle(models.Model):
    title = models.CharField(max_length=100)

class ContactHoverEffect(models.Model):
    title1 = models.CharField(max_length=50)
    description1 = models.CharField(max_length=600)
    title2 = models.CharField(max_length=50)
    description2 = models.CharField(max_length=600)
    title3 = models.CharField(max_length=50)
    description3 = models.CharField(max_length=600)

class ContactLastsection(models.Model):
    title = models.TextField(max_length=100)

# ===== Contact Page ====  #


# ===== Privacy Policy Page ====  #
class PrivacyBg(models.Model):
    img = models.ImageField(upload_to='images')
class PrivacyTitle(models.Model):
    title1 = models.CharField(max_length=50)
    title2 = models.CharField(max_length=50)



class PrivacySectionOne(models.Model):
    title = models.CharField(max_length=50)
    description1 = models.CharField(max_length=600)
    description2 = models.CharField(max_length=600)



class PrivacySectionTwo(models.Model):
    title = models.CharField(max_length=50)
    description1 = models.CharField(max_length=600)
    description2 = models.CharField(max_length=600)
    description3 = models.CharField(max_length=600)
    description4 = models.CharField(max_length=600)
    description5 = models.CharField(max_length=600)


class PrivacySectionthree(models.Model):
    title = models.CharField(max_length=50)
    description1 = models.CharField(max_length=600)
    description2 = models.CharField(max_length=600)
    description3 = models.CharField(max_length=600)


class PrivacySectionFour(models.Model):
    title = models.CharField(max_length=50)
    description1 = models.CharField(max_length=600)
    description2 = models.CharField(max_length=600)
    description3 = models.CharField(max_length=600)


class PrivacySectionfifth(models.Model):
    title = models.CharField(max_length=50)
    description1 = models.CharField(max_length=600)

class PrivacySectionSixth(models.Model):
    title = models.CharField(max_length=50)
    description1 = models.CharField(max_length=600)


class PrivacyLastsection(models.Model):
    title = models.CharField(max_length=150)

# ===== Privacy Policy Page ====  #
# ===== FAQ  Page ====  #
class FaqTitle(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=600)

class FaqQuestion(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=600)

class FaqLeftQuestions(models.Model):
    title1 = models.CharField(max_length=50)
    description1 = models.TextField(max_length=600)
    title2 = models.CharField(max_length=50)
    description2 = models.TextField(max_length=600)

class FaqLastsection(models.Model):
    title = models.TextField(max_length=100)
# ===== FAQ  Page ====  #


# === Contact Form === #

class ContactsForm(models.Model):
    yourName = models.TextField(max_length=50)
    email = models.EmailField()
    Phonenumber = models.CharField(max_length=20)
    Subject = models.CharField(max_length=100)
    companyname = models.TextField(max_length=50, blank=True, null=True)
    budget = models.CharField(max_length=100, blank=True, null=True)
    Message = models.CharField(max_length=400)

# === Contact Form === #
# === Blog Page === #
class Blogtitle(models.Model):
    title = models.CharField(max_length=50)

class BlogSubscribe(models.Model):
    email = models.EmailField()


class MainBlog(models.Model):
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images')
    Shortdescription = models.TextField(max_length=200)
    description1 = models.TextField(max_length=6000)
    description2 = models.TextField(max_length=6000)
    description3 = models.TextField(max_length=6000)
    relatedimg1 = models.ImageField(upload_to='images')
    relatedimg2 = models.ImageField(upload_to='images')
    relatedimg3 = models.ImageField(upload_to='images')
    relatedimg4 = models.ImageField(upload_to='images')
    relatedimg5 = models.ImageField(upload_to='images')
    relatedimg6 = models.ImageField(upload_to='images')
    description7 = models.TextField(max_length=8000)

    
class BlogLastSection(models.Model):
    title = models.CharField(max_length=100)

CATEGORY_CHOICES = (
    ('seo','SEO'),
    ('GraphiceDesigning','GRAPHICSDESIGNING'),
    ('digitalmarketing','digitalmarketing'),
    ('WebDevelopment','WEBDEVELOPMENT'),
    ('contentwriting','contentwriting'),
    ('videoediting','videoEditing'),
)
class Porftoliotitle(models.Model):
    title = models.TextField(max_length=400)

class PorftolioCategoie(models.Model):
    img = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100)
    className = models.CharField(max_length=100)

class PorftolioCategorie(models.Model):
    img = models.ImageField(upload_to='images')
    video = models.FileField(upload_to='images',null=True,blank=True)
    visititle = models.CharField(max_length=100,  null=True,blank=True)
    visitUrl = models.CharField(max_length=100,  null=True,blank=True)
    title = models.CharField(max_length=100)
    className = models.CharField(max_length=100)
    category = models.CharField(max_length=30,choices=CATEGORY_CHOICES)



class PorftolioSection(models.Model):
    title = models.CharField(max_length=100)
# === Blog Page === #
# === SLider SLider  === #
class HomeBg(models.Model):
    img = models.ImageField(upload_to='images')


class HomeSlidertitle(models.Model):
    title = models.CharField(max_length=100)
    sliderbg = models.ImageField(upload_to='images')
   
class HomeSlider(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=700)
# === SLider SLider  === #



# === footer  === #
class FootersectionOne(models.Model):
    title = models.CharField(max_length=100)
    subtitle1 = models.CharField(max_length=100)
    subtitle2 = models.CharField(max_length=100)
    subtitle3 = models.CharField(max_length=100)
    subtitle4 = models.CharField(max_length=100)
    subtitle5 = models.CharField(max_length=100)

class FootersectionTwo(models.Model):
    title = models.CharField(max_length=100)
    subtitle1 = models.CharField(max_length=100)
    subtitle2 = models.CharField(max_length=100)
    subtitle3 = models.CharField(max_length=100)
    subtitle4 = models.CharField(max_length=100)
    subtitle5 = models.CharField(max_length=100)


class FootersectionThree(models.Model):
    title = models.CharField(max_length=100)
    subtitle1 = models.CharField(max_length=100)
    subtitle2 = models.CharField(max_length=100)
    subtitle3 = models.CharField(max_length=100)
    subtitle4 = models.CharField(max_length=100)
    subtitle5 = models.CharField(max_length=100)


class FootersectionFour(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    
# === footer  === #

# === ICOn  === #
class ServicesAllIcon(models.Model):
    icon1 = models.ImageField(upload_to='images')
    icon2 = models.ImageField(upload_to='images')
    icon3 = models.ImageField(upload_to='images')
    icon4 = models.ImageField(upload_to='images')
    icon5 = models.ImageField(upload_to='images')
    icon6 = models.ImageField(upload_to='images')


# === ICOn  === #


class Thanks(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)






class StartProjectContactAllDetail(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    Phonenumber = models.CharField(max_length=100)
    PhoneUrl = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    






# ===== Privacy Policy Page ====  #
class TermsAndConditionBg(models.Model):
    img = models.ImageField(upload_to='images')

class TermsAndConditionTitle(models.Model):
    title1 = models.CharField(max_length=50)
    title2 = models.CharField(max_length=50)



class TermsAndConditionSectionOne(models.Model):
    title = models.CharField(max_length=50)
    description1 = models.CharField(max_length=600)
    description2 = models.CharField(max_length=600)



class TermsAndConditionSectionTwo(models.Model):
    title = models.CharField(max_length=50)
    description1 = models.CharField(max_length=600)
    description2 = models.CharField(max_length=600)
    description3 = models.CharField(max_length=600)
    description4 = models.CharField(max_length=600)
    description5 = models.CharField(max_length=600)


class TermsAndConditionSectionthree(models.Model):
    title = models.CharField(max_length=50)
    description1 = models.CharField(max_length=600)
    description2 = models.CharField(max_length=600)
    description3 = models.CharField(max_length=600)


class TermsAndConditionSectionFour(models.Model):
    title = models.CharField(max_length=50)
    description1 = models.CharField(max_length=600)
    description2 = models.CharField(max_length=600)
    description3 = models.CharField(max_length=600)


class TermsAndConditionSectionfifth(models.Model):
    title = models.CharField(max_length=50)
    description1 = models.CharField(max_length=600)

class TermsAndConditionSectionSixth(models.Model):
    title = models.CharField(max_length=50)
    description1 = models.CharField(max_length=600)


class TermsAndConditionLastsection(models.Model):
    title = models.CharField(max_length=150)

# ===== Privacy Policy Page ====  #