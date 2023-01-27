from django.contrib import admin
from .models import (
    Headeritem,
    NavLogo,
    Hometitle,
    Homeservicestitle,
    Homesectionthird,
    Homesectionfour,
    Homesectionfifth,
    Homesectionsixth,
    HomeBlog,
    HomeletDiscus,
    AboutBg,
    AboutTitle,
    AboutSectionTwo,
    AboutSectionthree,
    AboutSkill,
    AboutSectionfour,
    AboutSectionfifth,
    AboutSectionSixth,
    ServicesBg,
    ServicesTitle,
    ServicessectionTwo,
    ServicesCategorie,
    Servicessectionthree,
    ServicessectionSubthree,
    Servicessectionfour,
    ServicessectionSubfour,
    Servicessectionfifth,
    Servicessectionsixth,
    GraphicsServicesBg,
    GraphicsServicesTitle,
    GraphicsServicessectionTwo,
    GraphicsServicesCategorie,
    GraphicsAllIcons,
    GraphicsServicessectionthree,
    GraphicsServicessectionSubthree,
    GraphicsServicessectionfour,
    Graphicsfive,
    GraphicsSubfive,
    GraphicsServicessectionSubfour,
    GraphicsServicessectionfifth,
    GraphicsContact,
    GraphicsContactDetail,
    GraphicsServicessectionsixth,
    WebServicesBg,
    WebServicesTitle,
    WebServicessectionTwo,
    WebServicesCategorie,
    WebAllIcons,
    WebServicessectionthree,
    WebServicessectionSubthree,
    WebServicessectionfour,
    WebServicessectionSubfour,
    WebServicessectionfifth,
    WebServicessectionsixth,
    ContentServicesBg,
    ContentServicesTitle,
    ContentServicessectionTwo,
    ContentServicesCategorie,
    ContentWritingAllIcons,
    ContentServicessectionfive,
    ContentServicessectionSubfive,
    ContentServicessectionthree,
    ContentServicessectionSubthree,
    ContentServicessectionfour,
    ContentServicessectionSubfour,
    ContentServicessectionfifth,
    ContentServicessectionsixth,
    VideoEditingsectionthree,
    VideoEditingsectionSubthree,
    VideoEditingsectionfour,
    VideoEditingsectionSubfour,
    VideoEditingsectionfifth,
    VideoEditingsectionsixth,
    ContactBg,
    Contacttitle,
    ContactHoverEffect,
    ContactLastsection,
    ContactPhoneAndEmail,
    PrivacyBg,
    PrivacyTitle,
    PrivacySectionOne,
    PrivacySectionTwo,
    PrivacySectionthree,
    PrivacySectionFour,
    PrivacySectionfifth,
    PrivacySectionSixth,
    PrivacyLastsection,
    TermsAndConditionBg,
    TermsAndConditionTitle,
    TermsAndConditionSectionOne,
    TermsAndConditionSectionTwo,
    TermsAndConditionSectionthree,
    TermsAndConditionSectionFour,
    TermsAndConditionSectionfifth,
    TermsAndConditionSectionSixth,
    TermsAndConditionLastsection,
    FaqTitle,
    FaqQuestion,
    FaqLeftQuestions,
    FaqLastsection,
    ContactsForm,
    Blogtitle,
    BlogSubscribe,
    MainBlog,
    BlogLastSection,
    Porftoliotitle,
    PorftolioCategorie,
    PorftolioSection,
    HomeBg,
    HomeSlidertitle,
    HomeSlider,
    FootersectionOne,
    FootersectionTwo,
    FootersectionThree,
    FootersectionFour,
    ContactImg,
    VideoEditingBg,
    VideoEditingTitle,
    VideoEditingsectionTwo,
    VideoEditingCategorie,
    VideoEditingAllIcons,
    VideoEditingsectionthree,
    VideoEditingsectionSubthree,
    VideoEditingsectionfour,
    VideoEditingsectionSubfour,
    VideoEditingsectionfifth,
    VideoEditingsectionsixth,
    DigitalMarketingBg,
    DigitalMarketingTitle,
    DigitalMarketingsectionTwo,
    DigitalMarketingCategorie,
    DigitalMarketingsectionthree,
    DigitalMarketingSubthree,
    DigitalMarketingsectionfour,
    DigitalMarketingSubfour,
    DigitalMarketingsectionfifth,
    DigitalMarketingsectionsixth,
    SEOSEMBg,
    SEOSEMTitle,
    SEOSEMsectionTwo,
    SEOSEMCategorie,
    SEOSEMsectionthree,
    SEOSEMSubthree,
    SEOSEMsectionfour,
    SEOSEMSubfour,
    SEOSEMsectionfifth,
    SEOSEMsectionsixth,
    ServicesAllIcon,
    VideoEditingsectionfive,
    VideoEditingsectionSubfive,
    VideoEditingSixth,
    VideoEditingSubSixth,
    DigitalMarketingAllIcons,
    SeoSemAllIcons,
    SEOSEMSectionFive,
    SEOSEMSubtFive,
    HomeIcons,
    ContactIcons,
    Thanks,
    StartProjectContactAllDetail,
    Favicon,


)
@admin.register(Favicon)
class FaviconAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(StartProjectContactAllDetail)
class StartProjectContactAllDetailAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','Phonenumber','PhoneUrl','Email']


@admin.register(Thanks)
class ThanksAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']

@admin.register(HomeIcons)
class HomeIconsAdmin(admin.ModelAdmin):
    list_display = ['id','icon1','icon2','icon3','icon4']


@admin.register(ContactIcons)
class ContactIconsAdmin(admin.ModelAdmin):
    list_display = ['id','icon1','icon2','icon3']


@admin.register(SeoSemAllIcons)
class SeoSemAllIconsAdmin(admin.ModelAdmin):
    list_display = ['id','icon1','icon2',
    'icon3','icon4','icon5','icon6',
'icon7','icon8','icon9']

@admin.register(SEOSEMSectionFive)
class SEOSEMSectionFiveAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(SEOSEMSubtFive)
class SEOSEMSubtFiveAdmin(admin.ModelAdmin):
    list_display = ['id','title1','description1','title2','description2','title3','description3']

@admin.register(DigitalMarketingAllIcons)
class DigitalMarketingAllIconsAdmin(admin.ModelAdmin):
    list_display = ['id','icon1','icon2','icon3','icon4','icon5','icon6']

@admin.register(VideoEditingsectionSubfive)
class VideoEditingsectionSubfiveAdmin(admin.ModelAdmin):
    list_display = ['id','title1','description1','title2','description2','title3','description3']

@admin.register(VideoEditingSubSixth)
class VideoEditingsectionSubfiveAdmin(admin.ModelAdmin):
    list_display = ['id','title1','description1','title2','description2','title3','description3']

@admin.register(VideoEditingAllIcons)
class VideoEditingAllIconsAdmin(admin.ModelAdmin):
        list_display = ['id','icon1','icon2','icon3','icon4','icon5','icon6','icon7','icon8','icon9','icon10','icon11','icon12']

@admin.register(ServicesAllIcon)
class ServicesAllIconAdmin(admin.ModelAdmin):
    list_display = ['id','icon1','icon2','icon3','icon4','icon5','icon6']

@admin.register(VideoEditingsectionfive)
class VideoEditingsectionfiveAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(VideoEditingSixth)
class VideoEditingSixthAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(GraphicsAllIcons)
class GraphicsAllIconsAdmin(admin.ModelAdmin):
    list_display = ['id','icon1','icon2','icon3','icon4','icon5','icon6']


@admin.register(WebAllIcons)
class WebAllIconsAdmin(admin.ModelAdmin):
    list_display = ['id','icon1','icon2','icon3','icon4','icon5','icon6']


@admin.register(ContentWritingAllIcons)
class ContentWritingAllIconsAdmin(admin.ModelAdmin):
    list_display = ['id','icon1','icon2','icon3','icon4','icon5','icon6']


@admin.register(Graphicsfive)
class GraphicsfiveAdmin(admin.ModelAdmin):
    list_display = ['id','img']


@admin.register(GraphicsSubfive)
class GraphicsSubfiveAdmin(admin.ModelAdmin):
    list_display = ['id','title1','description1','title2','description2','title3','description3']




@admin.register(ContentServicessectionfive)
class ContentServicessectionfiveAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(ContentServicessectionSubfive)
class ContentServicessectionSubfiveAdmin(admin.ModelAdmin):
    list_display = ['id','title1','description1','title2','description2','title3','description3']




@admin.register(ContactPhoneAndEmail)
class ContactPhoneAndEmailAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','PhoneNumber','PhoneNumberUrl','email']



@admin.register(Headeritem)
class HeaderitemAdmin(admin.ModelAdmin):
    list_display = ['id','PhoneNumber','PhoneNumberUrl','Email']


@admin.register(NavLogo)
class NavLogoAdmin(admin.ModelAdmin):
    list_display = ['id','logo']

@admin.register(HomeBg)
class HomeBgAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(Hometitle)
class HometitleAdmin(admin.ModelAdmin):
    list_display = ['id','title1','title2','title3','description1','description1']


@admin.register(Homeservicestitle)
class HomeservicestitleAdmin(admin.ModelAdmin):
    list_display = ['id','title','subtitle1','description1','subtitle2','description2','subtitle3','description3']








@admin.register(Homesectionthird)
class HomesectionthirdAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','img','subtitle1','subtitle1','subdescription1','subtitle2','subdescription2']




@admin.register(Homesectionfour)
class HomesectionfourAdmin(admin.ModelAdmin):
    list_display = ['id','title','img','meter1','subtitle1','subdescription1','meter2','subtitle2','subdescription2']


@admin.register(Homesectionfifth)
class HomesectionfifthAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','img','subtitle1','subtitle1','subdescription1','subtitle2','subdescription2']




@admin.register(Homesectionsixth)
class HomesectionsixthAdmin(admin.ModelAdmin):
    list_display = ['id','title','description',]

@admin.register(HomeBlog)
class HomeBlogAdmin(admin.ModelAdmin):
    list_display = ['id','img','title']


@admin.register(HomeletDiscus)
class HomeletDiscusAdmin(admin.ModelAdmin):
    list_display = ['id','title']


# === Contact Form ==== #
@admin.register(ContactsForm)
class ContactForm(admin.ModelAdmin):
    list_display = ['id','yourName','companyname','budget','email','Phonenumber','Subject','Message',]

# === Contact Form ==== #




# ===== ABout section  ==== #

@admin.register(AboutBg)
class AboutBgAdmin(admin.ModelAdmin):
    list_display = ['id','img','video']

@admin.register(AboutTitle)
class AboutTitleAdmin(admin.ModelAdmin):
    list_display = ['id','title']

@admin.register(AboutSectionTwo)
class AboutSectionTwoAdmin(admin.ModelAdmin):
    list_display = ['id','title','description1','description2']

@admin.register(AboutSectionthree)
class AboutSectionthreeAdmin(admin.ModelAdmin):
    list_display = ['id','title','img']

@admin.register(AboutSkill)
class AboutSkillAdmin(admin.ModelAdmin):
    list_display = ['id','skill','percentage']

@admin.register(AboutSectionfour)
class AboutSectionfourAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','subtitle1','description1','subtitle2',
    'description2','subtitle3','description3','subtitle4','description4']

@admin.register(AboutSectionfifth)
class AboutSectionfifthAdmin(admin.ModelAdmin):
    list_display = ['id','img','title','meter1','subtitle1','subdescription1','meter2','subtitle2','subdescription2']


@admin.register(AboutSectionSixth)
class AboutSectionSixthAdmin(admin.ModelAdmin):
    list_display = ['id','title']


# ===== ABout section  ==== #


@admin.register(ServicesBg)
class ServicesBgAdmin(admin.ModelAdmin):
    list_display = ['id','img','video']

@admin.register(ServicesTitle)
class ServicesTitleAdmin(admin.ModelAdmin):
    list_display = ['id','title']


@admin.register(ServicessectionTwo)
class ServicessectionTwoAdmin(admin.ModelAdmin):
    list_display = ['id','title','description1','description2']

@admin.register(ServicesCategorie)
class ServicesCategorieAdmin(admin.ModelAdmin):
    list_display = ['id','title1','title2','title3','title4','title5','title6']

@admin.register(Servicessectionthree)
class ServicessectionthreeAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(ServicessectionSubthree)
class ServicessectionSubthreeAdmin(admin.ModelAdmin):
    list_display = ['id','title1','description1','title2','description2','title3','description3']

@admin.register(Servicessectionfour)
class ServicessectionfourAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(ServicessectionSubfour)
class ServicessectionSubfourAdmin(admin.ModelAdmin):
    list_display = ['id','title1','description1','title2','description2','title3','description3']

@admin.register(Servicessectionfifth)
class ServicessectionfifthAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']


@admin.register(Servicessectionsixth)
class ServicessectionsixthAdmin(admin.ModelAdmin):
    list_display = ['id','title']


# ==== content Services ==== #
@admin.register(ContentServicesBg)
class ContentServicesBgAdmin(admin.ModelAdmin):
    list_display = ['id','img','video']

@admin.register(ContentServicesTitle)
class ContentServicesTitleAdmin(admin.ModelAdmin):
    list_display = ['id','title']


@admin.register(ContentServicessectionTwo)
class ContentServicessectionTwoAdmin(admin.ModelAdmin):
    list_display = ['id','title','description1','description2']

@admin.register(ContentServicesCategorie)
class ContentServicesCategorieAdmin(admin.ModelAdmin):
    list_display = ['id','title1','title2','title3','title4','title5','title6','title7','title8','title9']

@admin.register(ContentServicessectionthree)
class ContentServicessectionthreeAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(ContentServicessectionSubthree)
class ContentServicessectionSubthreeAdmin(admin.ModelAdmin):
    list_display = ['id','title1','description1','title2','description2','title3','description3']

@admin.register(ContentServicessectionfour)
class ContentServicessectionfourAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(ContentServicessectionSubfour)
class ContentServicessectionSubfourAdmin(admin.ModelAdmin):
    list_display = ['id','title1','description1','title2','description2','title3','description3']

@admin.register(ContentServicessectionfifth)
class ContentServicessectionfifthAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']


@admin.register(ContentServicessectionsixth)
class ContentServicessectionsixthAdmin(admin.ModelAdmin):
    list_display = ['id','title']

# === content Writing === #

@admin.register(WebServicesBg)
class WebServicesBgAdmin(admin.ModelAdmin):
    list_display = ['id','img','video']

@admin.register(WebServicesTitle)
class WebServicesTitleAdmin(admin.ModelAdmin):
    list_display = ['id','title']


@admin.register(WebServicessectionTwo)
class WebServicessectionTwoAdmin(admin.ModelAdmin):
    list_display = ['id','title','description1','description2']

@admin.register(WebServicesCategorie)
class WebServicesCategorieAdmin(admin.ModelAdmin):
    list_display = ['id','title1','title2','title3','title4','title5','title6']

@admin.register(WebServicessectionthree)
class WebServicessectionthreeAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(WebServicessectionSubthree)
class WebServicessectionSubthreeAdmin(admin.ModelAdmin):
    list_display = ['id','title1','description1','title2','description2','title3','description3']

@admin.register(WebServicessectionfour)
class WebServicessectionfourAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(WebServicessectionSubfour)
class WebServicessectionSubfourAdmin(admin.ModelAdmin):
    list_display = ['id','title1','description1','title2','description2','title3','description3']

@admin.register(WebServicessectionfifth)
class WebServicessectionfifthAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']


@admin.register(WebServicessectionsixth)
class WebServicessectionsixthAdmin(admin.ModelAdmin):
    list_display = ['id','title']

# ==== WEb Services ==== #




# ===  Graphics === #
@admin.register(GraphicsServicesBg)
class GraphicsServicesBgAdmin(admin.ModelAdmin):
    list_display = ['id','img','video']

@admin.register(GraphicsServicesTitle)
class GraphicsServicesTitleAdmin(admin.ModelAdmin):
    list_display = ['id','title']


@admin.register(GraphicsServicessectionTwo)
class GraphicsServicessectionTwoAdmin(admin.ModelAdmin):
    list_display = ['id','title','description1','description2']

@admin.register(GraphicsServicesCategorie)
class GraphicsServicesCategorieAdmin(admin.ModelAdmin):
    list_display = ['id','title1','title2','title3','title4','title5','title6','title7','title8','title9']

@admin.register(GraphicsServicessectionthree)
class GraphicsServicessectionthreeAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(GraphicsServicessectionSubthree)
class GraphicsServicessectionSubthreeAdmin(admin.ModelAdmin):
    list_display = ['id','title1','description1','title2','description2','title3','description3']

@admin.register(GraphicsServicessectionfour)
class GraphicsServicessectionfourAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(GraphicsServicessectionSubfour)
class GraphicsServicessectionSubfourAdmin(admin.ModelAdmin):
    list_display = ['id','title1','description1','title2','description2','title3','description3']

@admin.register(GraphicsServicessectionfifth)
class GraphicsServicessectionfifthAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']

@admin.register(GraphicsServicessectionsixth)
class GraphicsServicessectionsixthAdmin(admin.ModelAdmin):
    list_display = ['id','title']


@admin.register(GraphicsContactDetail)
class GraphicsContactDetailAdmin(admin.ModelAdmin):
    list_display = ['id','PhoneNumber','PhoneUrl','email']


@admin.register(GraphicsContact)
class GraphicsServicessectionsixthAdmin(admin.ModelAdmin):
    list_display = ['id','img','title','description']

    
# ==== END GRAPHICS === #
@admin.register(ContactImg)
class ContactImgAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(ContactBg)
class ContactBgAdmin(admin.ModelAdmin):
    list_display = ['id','img','video']

@admin.register(Contacttitle)
class ContacttitleAdmin(admin.ModelAdmin):
    list_display = ['id','title']


@admin.register(ContactHoverEffect)
class ContactHoverEffectAdmin(admin.ModelAdmin):
    list_display = ['id','title1','description1','title2','description2','title3','description3']

@admin.register(ContactLastsection)
class ContactLastsectionAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    


@admin.register(PrivacyBg)
class PrivacyBgAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(PrivacyTitle)
class PrivacyTitleAdmin(admin.ModelAdmin):
    list_display = ['id','title1','title2']


@admin.register(PrivacySectionOne)
class PrivacySectionOneAdmin(admin.ModelAdmin):
    list_display = ['id','title','description1','description2']


@admin.register(PrivacySectionTwo)
class PrivacySectionTwoAdmin(admin.ModelAdmin):
    list_display = ['id','title','description1','description2','description3','description4','description5']

@admin.register(PrivacySectionthree)
class PrivacySectionthreeAdmin(admin.ModelAdmin):
    list_display = ['id','title','description1','description2','description3']

@admin.register(PrivacySectionFour)
class PrivacySectionFourAdmin(admin.ModelAdmin):
    list_display = ['id','title','description1','description2','description3']



@admin.register(PrivacySectionfifth)
class PrivacySectionfifthAdmin(admin.ModelAdmin):
    list_display = ['id','title','description1',]

@admin.register(PrivacySectionSixth)
class PrivacySectionSixthAdmin(admin.ModelAdmin):
    list_display = ['id','title','description1']

@admin.register(PrivacyLastsection)
class PrivacyLastsectionAdmin(admin.ModelAdmin):
    list_display = ['id','title']



@admin.register(TermsAndConditionBg)
class TermsAndConditionBgAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(TermsAndConditionTitle)
class TermsAndConditionTitleAdmin(admin.ModelAdmin):
    list_display = ['id','title1','title2']


@admin.register(TermsAndConditionSectionOne)
class TermsAndConditionSectionOneAdmin(admin.ModelAdmin):
    list_display = ['id','title','description1','description2']


@admin.register(TermsAndConditionSectionTwo)
class TermsAndConditionSectionTwoAdmin(admin.ModelAdmin):
    list_display = ['id','title','description1','description2','description3','description4','description5']

@admin.register(TermsAndConditionSectionthree)
class TermsAndConditionSectionthreeAdmin(admin.ModelAdmin):
    list_display = ['id','title','description1','description2','description3']

@admin.register(TermsAndConditionSectionFour)
class TermsAndConditionSectionFourAdmin(admin.ModelAdmin):
    list_display = ['id','title','description1','description2','description3']



@admin.register(TermsAndConditionSectionfifth)
class TermsAndConditionSectionfifthAdmin(admin.ModelAdmin):
    list_display = ['id','title','description1',]

@admin.register(TermsAndConditionSectionSixth)
class TermsAndConditionSectionSixthAdmin(admin.ModelAdmin):
    list_display = ['id','title','description1']

@admin.register(TermsAndConditionLastsection)
class TermsAndConditionLastsectionAdmin(admin.ModelAdmin):
    list_display = ['id','title']


@admin.register(FaqTitle)
class FaqTitleAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']

@admin.register(FaqQuestion)
class FaqQuestionAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']

@admin.register(FaqLeftQuestions)
class FaqLeftQuestionsAdmin(admin.ModelAdmin):
    list_display = ['id','title1','description1','title2','description2']

@admin.register(FaqLastsection)
class FaqLastsectionAdmin(admin.ModelAdmin):
    list_display = ['id','title']



@admin.register(Blogtitle)
class BlogtitleAmin(admin.ModelAdmin):
    list_display = ['id','title']


@admin.register(BlogSubscribe)
class BlogSubscribeAdmin(admin.ModelAdmin):
    list_display = ['id','email']


@admin.register(MainBlog)
class MainBlogAdmin(admin.ModelAdmin):
    list_display = ['id','title','date',
    'img','Shortdescription','description1',
    'description2','description3','relatedimg1',
    'relatedimg2','relatedimg3','relatedimg4','relatedimg5','relatedimg6','description7']

@admin.register(BlogLastSection)
class BlogLastSectionAdmin(admin.ModelAdmin):
    list_display = ['id','title']




@admin.register(Porftoliotitle)
class PorftoliotitleAdmin(admin.ModelAdmin):
    list_display = ['id','title']

@admin.register(PorftolioCategorie)
class PorftolioCategorieAdmin(admin.ModelAdmin):
    list_display = ['id','img','title','className','category']

@admin.register(PorftolioSection)
class PorftolioSectionAdmin(admin.ModelAdmin):
    list_display = ['id','title']




@admin.register(HomeSlidertitle)
class HomeSlidertitleAdmin(admin.ModelAdmin):
    list_display = ['id','sliderbg','title']
@admin.register(HomeSlider)
class HomeSlidertitleAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']




@admin.register(FootersectionOne)
class FootersectionOneAdmin(admin.ModelAdmin):
    list_display = ['id','title','subtitle1','subtitle2','subtitle3','subtitle4','subtitle5']


@admin.register(FootersectionTwo)
class FootersectionTwoAdmin(admin.ModelAdmin):
    list_display = ['id','title','subtitle1','subtitle2','subtitle3','subtitle4','subtitle5'] 

@admin.register(FootersectionThree)
class FootersectionTwoAdmin(admin.ModelAdmin):
    list_display = ['id','title','subtitle1','subtitle2','subtitle3','subtitle4','subtitle5'] 


@admin.register(FootersectionFour)
class FootersectionTwoAdmin(admin.ModelAdmin):
    list_display = ['id','title','description'] 



@admin.register(VideoEditingBg)
class VideoEditingBgServicesBgAdmin(admin.ModelAdmin):
    list_display = ['id','img','video']

@admin.register(VideoEditingTitle)
class VideoEditingTitleServicesTitleAdmin(admin.ModelAdmin):
    list_display = ['id','title']


@admin.register(VideoEditingsectionTwo)
class VideoEditingsectionTwoServicessectionTwoAdmin(admin.ModelAdmin):
    list_display = ['id','title','description1','description2']

@admin.register(VideoEditingCategorie)
class VideoEditingCategorieServicesCategorieAdmin(admin.ModelAdmin):
    list_display = ['id','title1','title2','title3','title4','title5','title6','title7','title8','title9','title10','title11','title12']

@admin.register(VideoEditingsectionthree)
class VideoEditingsectionthreeServicessectionthreeAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(VideoEditingsectionSubthree)
class VideoEditingsectionSubthreeAdmin(admin.ModelAdmin):
    list_display = ['id','title1','description1','title2','description2','title3','description3']

@admin.register(VideoEditingsectionfour)
class VideoEditingsectionfourfourAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(VideoEditingsectionSubfour)
class VideoEditingsectionSubfourAdmin(admin.ModelAdmin):
    list_display = ['id','title1','description1','title2','description2','title3','description3']

@admin.register(VideoEditingsectionfifth)
class VideoEditingsectionfifthAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']


@admin.register(VideoEditingsectionsixth)
class VideoEditingsectionsixthhAdmin(admin.ModelAdmin):
    list_display = ['id','title']


@admin.register(DigitalMarketingBg)
class DigitalMarketingBgAdmin(admin.ModelAdmin):
    list_display = ['id','img','video']

@admin.register(DigitalMarketingTitle)
class DigitalMarketingTitleAdmin(admin.ModelAdmin):
    list_display = ['id','title']


@admin.register(DigitalMarketingsectionTwo)
class DigitalMarketingsectionTwoAdmin(admin.ModelAdmin):
    list_display = ['id','title','description1','description2']

@admin.register(DigitalMarketingCategorie)
class DigitalMarketingCategorieAdmin(admin.ModelAdmin):
    list_display = ['id','title1','title2','title3','title4','title5','title6']

@admin.register(DigitalMarketingsectionthree)
class DigitalMarketingsectionthreeAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(DigitalMarketingSubthree)
class DigitalMarketingSubthreeAdmin(admin.ModelAdmin):
    list_display = ['id','title1','description1','title2','description2','title3','description3']

@admin.register(DigitalMarketingsectionfour)
class DigitalMarketingsectionfourAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(DigitalMarketingSubfour)
class DigitalMarketingSubfourAdmin(admin.ModelAdmin):
    list_display = ['id','title1','description1','title2','description2','title3','description3']

@admin.register(DigitalMarketingsectionfifth)
class DigitalMarketingsectionfifthAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']


@admin.register(DigitalMarketingsectionsixth)
class DigitalMarketingsectionsixthAdmin(admin.ModelAdmin):
    list_display = ['id','title']




@admin.register(SEOSEMBg)
class SEOSEMBgAdmin(admin.ModelAdmin):
    list_display = ['id','img','video']

@admin.register(SEOSEMTitle)
class SEOSEMTitleAdmin(admin.ModelAdmin):
    list_display = ['id','title']


@admin.register(SEOSEMsectionTwo)
class SEOSEMsectionTwoAdmin(admin.ModelAdmin):
    list_display = ['id','title','description1','description2']

@admin.register(SEOSEMCategorie)
class SEOSEMCategorieAdmin(admin.ModelAdmin):
    list_display = ['id','title1','title2','title3','title4','title5','title6','title7','title8','title9']

@admin.register(SEOSEMsectionthree)
class SEOSEMsectionthreeAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(SEOSEMSubthree)
class SEOSEMSubthreeAdmin(admin.ModelAdmin):
    list_display = ['id','title1','description1','title2','description2','title3','description3']

@admin.register(SEOSEMsectionfour)
class SEOSEMsectionfourAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(SEOSEMSubfour)
class SEOSEMSubfourAdmin(admin.ModelAdmin):
    list_display = ['id','title1','description1','title2','description2','title3','description3']

@admin.register(SEOSEMsectionfifth)
class SEOSEMsectionfifthAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']


@admin.register(SEOSEMsectionsixth)
class SEOSEMsectionsixthAdmin(admin.ModelAdmin):
    list_display = ['id','title']


