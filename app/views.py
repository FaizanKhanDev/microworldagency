from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .forms import ContactUs,BlogEmail
from django.contrib import messages
from .models import (
    Favicon,
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

)


def seosem(request):
    favicon = Favicon.objects.all()
    headeritem = Headeritem.objects.all()
    navLogo = NavLogo.objects.all()
    servicesBg = SEOSEMBg.objects.all()
    servicesTitle = SEOSEMTitle.objects.all()
    servicessectionTwo = SEOSEMsectionTwo.objects.all()
    servicesCategorie = SEOSEMCategorie.objects.all()
    servicessectionthree = SEOSEMsectionthree.objects.all()
    servicessectionSubthree = SEOSEMSubthree.objects.all()
    servicessectionfour = SEOSEMsectionfour.objects.all()
    servicessectionSubfour = SEOSEMSubfour.objects.all()
    servicessectionfifth = SEOSEMsectionfifth.objects.all()
    seoSemAllIcons = SeoSemAllIcons.objects.all()
    sEOSEMSectionFive = SEOSEMSectionFive.objects.all()
    sEOSEMSubtFive = SEOSEMSubtFive.objects.all()
    contactPhoneAndEmail = ContactPhoneAndEmail.objects.all()
    contactImg = ContactImg.objects.all()
    servicessectionsixth = SEOSEMsectionsixth.objects.all()
    footersectionOne = FootersectionOne.objects.all()
    footersectionTwo = FootersectionTwo.objects.all()
    footersectionThree = FootersectionThree.objects.all()
    footersectionFour = FootersectionFour.objects.all()
    startProjectContactAllDetail = StartProjectContactAllDetail.objects.all()
    if request.method == 'POST':
        form = ContactUs (request.POST)
        if form.is_valid():
            yn = form.cleaned_data['yourName']
            em = form.cleaned_data['email']
            cn = form.cleaned_data['companyname']
            bd = form.cleaned_data['budget']
            pn = form.cleaned_data['Phonenumber']
            sb = form.cleaned_data['Subject']
            me = form.cleaned_data['Message']
            reg = ContactsForm(yourName=yn,email=em,companyname=cn,budget=bd,Phonenumber=pn,Subject=sb,Message=me)
            reg.save()
            form = ContactUs()
            return redirect ('/thankyou/')        

    else:
        form = ContactUs()
    return render (request,'app/seosem.html',{
        'favicon':favicon,
        'headeritem': headeritem,
        'navLogo':navLogo,
        'startProjectContactAllDetail':startProjectContactAllDetail,
        'servicesBg':servicesBg,
        'servicesTitle':servicesTitle,
        'servicessectionTwo':servicessectionTwo,
        'servicesCategorie':servicesCategorie,
        'servicessectionthree':servicessectionthree,
        'servicessectionSubthree':servicessectionSubthree,
        'servicessectionfour':servicessectionfour,
        'servicessectionSubfour':servicessectionSubfour,
        'servicessectionfifth':servicessectionfifth,
        'seoSemAllIcons':seoSemAllIcons,
        'sEOSEMSectionFive':sEOSEMSectionFive,
        'sEOSEMSubtFive':sEOSEMSubtFive,
        'contactPhoneAndEmail':contactPhoneAndEmail,
        'contactImg':contactImg,
        'servicessectionsixth':servicessectionsixth,
        'form':form,
        'footersectionOne':footersectionOne,
        'footersectionTwo':footersectionTwo,
        'footersectionThree':footersectionThree,
        'footersectionFour':footersectionFour,
    })








def digitalmarketing(request):
    favicon = Favicon.objects.all()
    headeritem = Headeritem.objects.all()
    navLogo = NavLogo.objects.all()
    startProjectContactAllDetail = StartProjectContactAllDetail.objects.all()
    servicesBg = DigitalMarketingBg.objects.all()
    servicesTitle = DigitalMarketingTitle.objects.all()
    servicessectionTwo = DigitalMarketingsectionTwo.objects.all()
    servicesCategorie = DigitalMarketingCategorie.objects.all()
    servicessectionthree = DigitalMarketingsectionthree.objects.all()
    servicessectionSubthree = DigitalMarketingSubthree.objects.all()
    servicessectionfour = DigitalMarketingsectionfour.objects.all()
    servicessectionSubfour = DigitalMarketingSubfour.objects.all()
    digitalMarketingAllIcons = DigitalMarketingAllIcons.objects.all()
    servicessectionfifth = DigitalMarketingsectionfifth.objects.all()
    contactPhoneAndEmail = ContactPhoneAndEmail.objects.all()
    contactImg = ContactImg.objects.all()
    servicessectionsixth = DigitalMarketingsectionsixth.objects.all()
    footersectionOne = FootersectionOne.objects.all()
    footersectionTwo = FootersectionTwo.objects.all()
    footersectionThree = FootersectionThree.objects.all()
    footersectionFour = FootersectionFour.objects.all()
    if request.method == 'POST':
        form = ContactUs (request.POST)
        if form.is_valid():
            yn = form.cleaned_data['yourName']
            em = form.cleaned_data['email']
            cn = form.cleaned_data['companyname']
            bd = form.cleaned_data['budget']
            pn = form.cleaned_data['Phonenumber']
            sb = form.cleaned_data['Subject']
            me = form.cleaned_data['Message']
            reg = ContactsForm(yourName=yn,email=em,companyname=cn,budget=bd,Phonenumber=pn,Subject=sb,Message=me)
            reg.save()
            form = ContactUs()
            return redirect ('/thankyou/')        

    else:
        form = ContactUs()
    return render (request,'app/digitalmarketing.html',{
        'headeritem': headeritem,
        'favicon':favicon,
        'navLogo':navLogo,
        'startProjectContactAllDetail':startProjectContactAllDetail,
        'servicesBg':servicesBg,
        'servicesTitle':servicesTitle,
        'servicessectionTwo':servicessectionTwo,
        'servicesCategorie':servicesCategorie,
        'digitalMarketingAllIcons':digitalMarketingAllIcons,
        'servicessectionthree':servicessectionthree,
        'servicessectionSubthree':servicessectionSubthree,
        'servicessectionfour':servicessectionfour,
        'servicessectionSubfour':servicessectionSubfour,
        'servicessectionfifth':servicessectionfifth,
        'contactPhoneAndEmail':contactPhoneAndEmail,
        'contactImg':contactImg,
        'servicessectionsixth':servicessectionsixth,
        'form':form,
        'footersectionOne':footersectionOne,
        'footersectionTwo':footersectionTwo,
        'footersectionThree':footersectionThree,
        'footersectionFour':footersectionFour,
    })








# ==== Home Page Render ==== #

def home(request):
    favicon = Favicon.objects.all()
    headeritem = Headeritem.objects.all()
    navLogo = NavLogo.objects.all()
    homeBg = HomeBg.objects.all()
    startProjectContactAllDetail = StartProjectContactAllDetail.objects.all()
    homeIcons = HomeIcons.objects.all()
    homettle = Hometitle.objects.all()
    homeServicestitle = Homeservicestitle.objects.all()
    homeSectionthird = Homesectionthird.objects.all()
    homeSectionfour = Homesectionfour.objects.all()
    homeSectionfifth = Homesectionfifth.objects.all()
    homeSectionsixth = Homesectionsixth.objects.all()
    homeblog = HomeBlog.objects.all()
    homeletDiscus = HomeletDiscus.objects.all()
    homeSlidertitle= HomeSlidertitle.objects.all()
    homeSlider= HomeSlider.objects.all()
    footersectionOne = FootersectionOne.objects.all()
    footersectionTwo = FootersectionTwo.objects.all()
    footersectionThree = FootersectionThree.objects.all()
    footersectionFour = FootersectionFour.objects.all()
    if request.method == 'POST':
        form = ContactUs (request.POST)
        if form.is_valid():
            yn = form.cleaned_data['yourName']
            em = form.cleaned_data['email']
            cn = form.cleaned_data['companyname']
            bd = form.cleaned_data['budget']
            pn = form.cleaned_data['Phonenumber']
            sb = form.cleaned_data['Subject']
            me = form.cleaned_data['Message']
            reg = ContactsForm(yourName=yn,email=em,companyname=cn,budget=bd,Phonenumber=pn,Subject=sb,Message=me)
            reg.save()
            form = ContactUs()  
            return redirect ('/thankyou/')        

    else:
        form = ContactUs()
    return render (request,'app/home.html',
    {       'favicon':favicon,
            'headeritem':headeritem,
            'navLogo':navLogo,
            'homeBg':homeBg,
            'homettle':homettle,
            'homeServicestitle':homeServicestitle,
            'homeSectionthird':homeSectionthird,
            'homeSectionfour':homeSectionfour,
            'homeSectionfifth':homeSectionfifth,
            'homeSectionsixth':homeSectionsixth,
            'homeblog':homeblog,
            'homeletDiscus':homeletDiscus,
            'homeSlidertitle':homeSlidertitle,
            'homeSlider':homeSlider,
            'form':form,
            'homeIcons':homeIcons,
            'footersectionOne':footersectionOne,
            'footersectionTwo':footersectionTwo,
            'footersectionThree':footersectionThree,
            'footersectionFour':footersectionFour,
            'startProjectContactAllDetail':startProjectContactAllDetail,
})


# ==== Home Page Render ==== #


# ==== About Page Render ==== #
def about(request):
    favicon = Favicon.objects.all()
    headeritem = Headeritem.objects.all()
    navLogo = NavLogo.objects.all()
    aboutBg = AboutBg.objects.all()
    aboutTitle = AboutTitle.objects.all()
    aboutSectionTwo = AboutSectionTwo.objects.all()
    aboutSectionthree = AboutSectionthree.objects.all()
    aboutSkill = AboutSkill.objects.all()
    aboutSectionfour = AboutSectionfour.objects.all()
    aboutSectionfifth = AboutSectionfifth.objects.all()
    aboutSectionSixth = AboutSectionSixth.objects.all()
    footersectionOne = FootersectionOne.objects.all()
    footersectionTwo = FootersectionTwo.objects.all()
    footersectionThree = FootersectionThree.objects.all()
    footersectionFour = FootersectionFour.objects.all()
    startProjectContactAllDetail = StartProjectContactAllDetail.objects.all()

    if request.method == 'POST':
        form = ContactUs (request.POST)
        if form.is_valid():
            yn = form.cleaned_data['yourName']
            em = form.cleaned_data['email']
            cn = form.cleaned_data['companyname']
            bd = form.cleaned_data['budget']
            pn = form.cleaned_data['Phonenumber']
            sb = form.cleaned_data['Subject']
            me = form.cleaned_data['Message']
            reg = ContactsForm(yourName=yn,email=em,companyname=cn,budget=bd,Phonenumber=pn,Subject=sb,Message=me)
            reg.save()
            form = ContactUs()  
            return redirect ('/thankyou/')        

    else:
        form = ContactUs()
    return render (request,'app/about.html',{
        'favicon':favicon,
        'headeritem':headeritem,
        'navLogo':navLogo,
        'aboutTitle' : aboutTitle,
        'aboutSectionTwo' : aboutSectionTwo,
        'aboutSectionthree' : aboutSectionthree,
        'aboutSkill' : aboutSkill,
        'aboutSectionfour' : aboutSectionfour,
        'aboutSectionfifth' : aboutSectionfifth,
        'aboutSectionSixth' : aboutSectionSixth,
        'form':form,
        'footersectionOne':footersectionOne,
        'footersectionTwo':footersectionTwo,
        'footersectionThree':footersectionThree,
        'footersectionFour':footersectionFour,
        'aboutBg':aboutBg,
        'startProjectContactAllDetail':startProjectContactAllDetail,

    })

# ==== About Page Render ==== #

# ==== services Page Render ==== #
def services(request):
    favicon = Favicon.objects.all()
    headeritem = Headeritem.objects.all()
    navLogo = NavLogo.objects.all()
    servicesBg = ServicesBg.objects.all()
    servicesTitle = ServicesTitle.objects.all()
    servicessectionTwo = ServicessectionTwo.objects.all()
    servicesCategorie = ServicesCategorie.objects.all()
    servicessectionthree = Servicessectionthree.objects.all()
    servicessectionSubthree = ServicessectionSubthree.objects.all()
    servicessectionfour = Servicessectionfour.objects.all()
    servicessectionSubfour = ServicessectionSubfour.objects.all()
    servicessectionfifth = Servicessectionfifth.objects.all()
    servicesAllIcon = ServicesAllIcon.objects.all()
    contactPhoneAndEmail = ContactPhoneAndEmail.objects.all()
    contactImg = ContactImg.objects.all()
    servicessectionsixth = Servicessectionsixth.objects.all()
    footersectionOne = FootersectionOne.objects.all()
    footersectionTwo = FootersectionTwo.objects.all()
    footersectionThree = FootersectionThree.objects.all()
    footersectionFour = FootersectionFour.objects.all()
    startProjectContactAllDetail = StartProjectContactAllDetail.objects.all()
    if request.method == 'POST':
        form = ContactUs (request.POST)
        if form.is_valid():
            yn = form.cleaned_data['yourName']
            em = form.cleaned_data['email']
            cn = form.cleaned_data['companyname']
            bd = form.cleaned_data['budget']
            pn = form.cleaned_data['Phonenumber']
            sb = form.cleaned_data['Subject']
            me = form.cleaned_data['Message']
            reg = ContactsForm(yourName=yn,email=em,companyname=cn,budget=bd,Phonenumber=pn,Subject=sb,Message=me)
            reg.save()
            form = ContactUs()
            return redirect ('/thankyou/')        

    else:
        form = ContactUs()
    return render (request,'app/services.html',{
        'favicon':favicon,
        'headeritem': headeritem,
        'navLogo':navLogo,
        'startProjectContactAllDetail':startProjectContactAllDetail,
        'servicesBg':servicesBg,
        'servicesTitle':servicesTitle,
        'servicessectionTwo':servicessectionTwo,
        'servicesCategorie':servicesCategorie,
        'servicessectionthree':servicessectionthree,
        'servicessectionSubthree':servicessectionSubthree,
        'servicessectionfour':servicessectionfour,
        'servicessectionSubfour':servicessectionSubfour,
        'servicessectionfifth':servicessectionfifth,
        'contactPhoneAndEmail':contactPhoneAndEmail,
        'contactImg':contactImg,
        'servicessectionsixth':servicessectionsixth,
        'servicesAllIcon':servicesAllIcon,
        'form':form,
        'footersectionOne':footersectionOne,
        'footersectionTwo':footersectionTwo,
        'footersectionThree':footersectionThree,
        'footersectionFour':footersectionFour,
    })

# ==== services Page Render ==== #
def videoediting(request):
    favicon = Favicon.objects.all()
    headeritem = Headeritem.objects.all()
    navLogo = NavLogo.objects.all()
    servicesBg = VideoEditingBg.objects.all()
    servicesTitle = VideoEditingTitle.objects.all()
    servicessectionTwo = VideoEditingsectionTwo.objects.all()
    servicesCategorie = VideoEditingCategorie.objects.all()
    videoeditingAllIcons = VideoEditingAllIcons.objects.all()
    servicessectionthree = VideoEditingsectionthree.objects.all()
    servicessectionSubthree = VideoEditingsectionSubthree.objects.all()
    servicessectionfour = VideoEditingsectionfour.objects.all()
    servicessectionSubfour = VideoEditingsectionSubfour.objects.all()
    servicessectionfifth = VideoEditingsectionfifth.objects.all()
    videoEditingsectionfive = VideoEditingsectionfive.objects.all()
    videoEditingsectionSubfive = VideoEditingsectionSubfive.objects.all()
    videoEditingSixth = VideoEditingSixth.objects.all()
    videoEditingSubSixth = VideoEditingSubSixth.objects.all()
    contactPhoneAndEmail = ContactPhoneAndEmail.objects.all()
    contactImg = ContactImg.objects.all()
    servicessectionsixth = VideoEditingsectionsixth.objects.all()
    footersectionOne = FootersectionOne.objects.all()
    footersectionTwo = FootersectionTwo.objects.all()
    footersectionThree = FootersectionThree.objects.all()
    footersectionFour = FootersectionFour.objects.all()
    startProjectContactAllDetail = StartProjectContactAllDetail.objects.all()
    if request.method == 'POST':
        form = ContactUs (request.POST)
        if form.is_valid():
            yn = form.cleaned_data['yourName']
            em = form.cleaned_data['email']
            cn = form.cleaned_data['companyname']
            bd = form.cleaned_data['budget']
            pn = form.cleaned_data['Phonenumber']
            sb = form.cleaned_data['Subject']
            me = form.cleaned_data['Message']
            reg = ContactsForm(yourName=yn,email=em,companyname=cn,budget=bd,Phonenumber=pn,Subject=sb,Message=me)
            reg.save()
            form = ContactUs()
            return redirect ('/thankyou/')        

    else:
        form = ContactUs()
    return render (request,'app/videoediting.html',{
        'favicon':favicon,
        'headeritem': headeritem,
        'navLogo':navLogo,
        'servicesBg':servicesBg,
        'startProjectContactAllDetail':startProjectContactAllDetail,
        'servicesTitle':servicesTitle,
        'servicessectionTwo':servicessectionTwo,
        'servicesCategorie':servicesCategorie,
        'videoeditingAllIcons':videoeditingAllIcons,
        'servicessectionthree':servicessectionthree,
        'servicessectionSubthree':servicessectionSubthree,
        'servicessectionfour':servicessectionfour,
        'servicessectionSubfour':servicessectionSubfour,
        'servicessectionfifth':servicessectionfifth,
        'contactPhoneAndEmail':contactPhoneAndEmail,
        'contactImg':contactImg,
        'servicessectionsixth':servicessectionsixth,
        'videoEditingsectionfive':videoEditingsectionfive,
        'videoEditingsectionSubfive':videoEditingsectionSubfive,
        'videoEditingSixth':videoEditingSixth,
        'videoEditingSubSixth':videoEditingSubSixth,
        'form':form,
        'footersectionOne':footersectionOne,
        'footersectionTwo':footersectionTwo,
        'footersectionThree':footersectionThree,
        'footersectionFour':footersectionFour,
    })

# == content Writing == #

def contentservices(request):
    favicon = Favicon.objects.all()
    headeritem = Headeritem.objects.all()
    navLogo = NavLogo.objects.all()
    startProjectContactAllDetail = StartProjectContactAllDetail.objects.all()
    servicesBg = ContentServicesBg.objects.all()
    servicesTitle = ContentServicesTitle.objects.all()
    servicessectionTwo = ContentServicessectionTwo.objects.all()
    servicesCategorie = ContentServicesCategorie.objects.all()
    contentWritingAllIcons = ContentWritingAllIcons.objects.all()
    servicessectionthree = ContentServicessectionthree.objects.all()
    servicessectionSubthree = ContentServicessectionSubthree.objects.all()
    servicessectionfour = ContentServicessectionfour.objects.all()
    servicessectionSubfour = ContentServicessectionSubfour.objects.all()
    contentServicessectionfive = ContentServicessectionfive.objects.all()
    contentServicessectionSubfive  = ContentServicessectionSubfive.objects.all()
    servicessectionfifth = ContentServicessectionfifth.objects.all()
    contactPhoneAndEmail = ContactPhoneAndEmail.objects.all()
    contactImg = ContactImg.objects.all()
    servicessectionsixth = ContentServicessectionsixth.objects.all()
    footersectionOne = FootersectionOne.objects.all()
    footersectionTwo = FootersectionTwo.objects.all()
    footersectionThree = FootersectionThree.objects.all()
    footersectionFour = FootersectionFour.objects.all()
    if request.method == 'POST':
        form = ContactUs (request.POST)
        if form.is_valid():
            yn = form.cleaned_data['yourName']
            em = form.cleaned_data['email']
            cn = form.cleaned_data['companyname']
            bd = form.cleaned_data['budget']
            pn = form.cleaned_data['Phonenumber']
            sb = form.cleaned_data['Subject']
            me = form.cleaned_data['Message']
            reg = ContactsForm(yourName=yn,email=em,companyname=cn,budget=bd,Phonenumber=pn,Subject=sb,Message=me)
            reg.save()
            form = ContactUs()
            return redirect ('/thankyou/')        

    else:
        form = ContactUs()
    return render (request,'app/contentwriting.html',{
        'favicon':favicon,
        'headeritem': headeritem,
        'navLogo':navLogo,
        'startProjectContactAllDetail':startProjectContactAllDetail,
        'servicesBg':servicesBg,
        'servicesTitle':servicesTitle,
        'servicessectionTwo':servicessectionTwo,
        'servicesCategorie':servicesCategorie,
        'contentWritingAllIcons':contentWritingAllIcons,
        'servicessectionthree':servicessectionthree,
        'servicessectionSubthree':servicessectionSubthree,
        'servicessectionfour':servicessectionfour,
        'servicessectionSubfour':servicessectionSubfour,
        'servicessectionfifth':servicessectionfifth,
        'contentServicessectionfive':contentServicessectionfive,
        'contentServicessectionSubfive':contentServicessectionSubfive,
        'contactPhoneAndEmail':contactPhoneAndEmail,
        'contactImg':contactImg,
        'servicessectionsixth':servicessectionsixth,
        'form':form,
        'footersectionOne':footersectionOne,
        'footersectionTwo':footersectionTwo,
        'footersectionThree':footersectionThree,
        'footersectionFour':footersectionFour,
    })
# == content Writing == #


def webservices(request):
    favicon = Favicon.objects.all()
    headeritem = Headeritem.objects.all()
    navLogo = NavLogo.objects.all()
    startProjectContactAllDetail = StartProjectContactAllDetail.objects.all()
    servicesBg = WebServicesBg.objects.all()
    servicesTitle = WebServicesTitle.objects.all()
    servicessectionTwo = WebServicessectionTwo.objects.all()
    servicesCategorie = WebServicesCategorie.objects.all()
    webAllIcons = WebAllIcons.objects.all()
    servicessectionthree = WebServicessectionthree.objects.all()
    servicessectionSubthree = WebServicessectionSubthree.objects.all()
    servicessectionfour = WebServicessectionfour.objects.all()
    servicessectionSubfour = WebServicessectionSubfour.objects.all()
    servicessectionfifth = WebServicessectionfifth.objects.all()
    contactPhoneAndEmail = ContactPhoneAndEmail.objects.all()
    contactImg = ContactImg.objects.all()
    servicessectionsixth = WebServicessectionsixth.objects.all()
    footersectionOne = FootersectionOne.objects.all()
    footersectionTwo = FootersectionTwo.objects.all()
    footersectionThree = FootersectionThree.objects.all()
    footersectionFour = FootersectionFour.objects.all()
    if request.method == 'POST':
        form = ContactUs (request.POST)
        if form.is_valid():
            yn = form.cleaned_data['yourName']
            em = form.cleaned_data['email']
            cn = form.cleaned_data['companyname']
            bd = form.cleaned_data['budget']
            pn = form.cleaned_data['Phonenumber']
            sb = form.cleaned_data['Subject']
            me = form.cleaned_data['Message']
            reg = ContactsForm(yourName=yn,email=em,companyname=cn,budget=bd,Phonenumber=pn,Subject=sb,Message=me)
            reg.save()
            form = ContactUs()
            return redirect ('/thankyou/')        

    else:
        form = ContactUs()
    return render (request,'app/webdevelopment.html',{
        'favicon':favicon,
        'startProjectContactAllDetail':startProjectContactAllDetail,
        'headeritem': headeritem,
        'navLogo':navLogo,
        'servicesBg':servicesBg,
        'servicesTitle':servicesTitle,
        'servicessectionTwo':servicessectionTwo,
        'servicesCategorie':servicesCategorie,
        'webAllIcons':webAllIcons,
        'servicessectionthree':servicessectionthree,
        'servicessectionSubthree':servicessectionSubthree,
        'servicessectionfour':servicessectionfour,
        'servicessectionSubfour':servicessectionSubfour,
        'servicessectionfifth':servicessectionfifth,
        'contactPhoneAndEmail':contactPhoneAndEmail,
        'contactImg':contactImg,
        'servicessectionsixth':servicessectionsixth,
        'form':form,
        'footersectionOne':footersectionOne,
        'footersectionTwo':footersectionTwo,
        'footersectionThree':footersectionThree,
        'footersectionFour':footersectionFour,
    })
# ==== Graphics services Page Render ==== #
def graphicsservices(request):
    favicon = Favicon.objects.all()
    headeritem = Headeritem.objects.all()
    navLogo = NavLogo.objects.all()
    startProjectContactAllDetail = StartProjectContactAllDetail.objects.all()
    servicesBg = GraphicsServicesBg.objects.all()
    servicesTitle = GraphicsServicesTitle.objects.all()
    servicessectionTwo = GraphicsServicessectionTwo.objects.all()
    servicesCategorie = GraphicsServicesCategorie.objects.all()
    graphicsAllIcons = GraphicsAllIcons.objects.all()
    servicessectionthree = GraphicsServicessectionthree.objects.all()
    servicessectionSubthree = GraphicsServicessectionSubthree.objects.all()
    servicessectionfour = GraphicsServicessectionfour.objects.all()
    servicessectionSubfour = GraphicsServicessectionSubfour.objects.all()
    graphicsfive = Graphicsfive.objects.all()
    graphicsSubfive = GraphicsSubfive.objects.all()
    servicessectionfifth = GraphicsServicessectionfifth.objects.all()
    graphicsContact = GraphicsContact.objects.all() 
    graphicsContactDetail = GraphicsContactDetail.objects.all()
    servicessectionsixth = GraphicsServicessectionsixth.objects.all()
    footersectionOne = FootersectionOne.objects.all()
    footersectionTwo = FootersectionTwo.objects.all()
    footersectionThree = FootersectionThree.objects.all()
    footersectionFour = FootersectionFour.objects.all()
    if request.method == 'POST':
        form = ContactUs (request.POST)
        if form.is_valid():
            yn = form.cleaned_data['yourName']
            em = form.cleaned_data['email']
            cn = form.cleaned_data['companyname']
            bd = form.cleaned_data['budget']
            pn = form.cleaned_data['Phonenumber']
            sb = form.cleaned_data['Subject']
            me = form.cleaned_data['Message']
            reg = ContactsForm(yourName=yn,email=em,companyname=cn,budget=bd,Phonenumber=pn,Subject=sb,Message=me)
            reg.save()
            form = ContactUs()
            return redirect ('/thankyou/')        
    else:
        form = ContactUs()
    return render (request,'app/graphics.html',{
        'favicon':favicon,
        'headeritem': headeritem,
        'navLogo':navLogo,
        'startProjectContactAllDetail':startProjectContactAllDetail,
        'servicesBg':servicesBg,
        'servicesTitle':servicesTitle,
        'servicessectionTwo':servicessectionTwo,
        'servicesCategorie':servicesCategorie,
        'graphicsAllIcons':graphicsAllIcons,
        'servicessectionthree':servicessectionthree,
        'servicessectionSubthree':servicessectionSubthree,
        'servicessectionfour':servicessectionfour,
        'servicessectionSubfour':servicessectionSubfour,
        'graphicsfive':graphicsfive,
        'graphicsSubfive':graphicsSubfive,
        'servicessectionfifth':servicessectionfifth,
        'graphicsContact':graphicsContact,
        'graphicsContactDetail':graphicsContactDetail,
        'servicessectionsixth':servicessectionsixth,
        'form':form,
        'footersectionOne':footersectionOne,
        'footersectionTwo':footersectionTwo,
        'footersectionThree':footersectionThree,
        'footersectionFour':footersectionFour,
    })

# ==== services Page Render ==== #
# ==== contactus Page Render ==== #
def contactus(request):
    favicon = Favicon.objects.all()
    headeritem = Headeritem.objects.all()
    navLogo = NavLogo.objects.all()
    startProjectContactAllDetail = StartProjectContactAllDetail.objects.all()
    contactIcons = ContactIcons.objects.all()
    contactBg = ContactBg.objects.all()
    contacttitle = Contacttitle.objects.all()
    contactHoverEffect = ContactHoverEffect.objects.all()
    contactLastsection = ContactLastsection.objects.all()
    contactPhoneAndEmail = ContactPhoneAndEmail.objects.all()
    contactImg = ContactImg.objects.all()
    footersectionOne = FootersectionOne.objects.all()
    footersectionTwo = FootersectionTwo.objects.all()
    footersectionThree = FootersectionThree.objects.all()
    footersectionFour = FootersectionFour.objects.all()
    if request.method == 'POST':
        form = ContactUs(request.POST)
        if form.is_valid():
                yn = form.cleaned_data['yourName']
                em = form.cleaned_data['email']
                cn = form.cleaned_data['companyname']
                bd = form.cleaned_data['budget']
                pn = form.cleaned_data['Phonenumber']
                sb = form.cleaned_data['Subject']
                me = form.cleaned_data['Message']
                reg = ContactsForm(yourName=yn,email=em,companyname=cn,budget=bd,Phonenumber=pn,Subject=sb,Message=me)
                reg.save()
                form = ContactUs()   
                return redirect ('/thankyou/')        
    else:
        form = ContactUs()
    return render (request,'app/contact.html',
{       
        'favicon':favicon,
        'headeritem': headeritem,
        'navLogo':navLogo,
        'contactBg':contactBg,
        'contacttitle':contacttitle,
        'contactHoverEffect':contactHoverEffect,
        'contactLastsection':contactLastsection,
        'contactPhoneAndEmail':contactPhoneAndEmail,
        'contactImg':contactImg,
        'form':form,
        'contactIcons':contactIcons,
        'footersectionOne':footersectionOne,
        'footersectionTwo':footersectionTwo,
        'footersectionThree':footersectionThree,
        'footersectionFour':footersectionFour,
        'startProjectContactAllDetail':startProjectContactAllDetail,
    })

# ==== contactus Page Render ==== #


# ==== blog Page Render ==== #
def blog(request):
    favicon = Favicon.objects.all()
    headeritem = Headeritem.objects.all()
    navLogo = NavLogo.objects.all()
    blogtitle=Blogtitle.objects.all()
    mainBlog = MainBlog.objects.all()
    blogLastSection = BlogLastSection.objects.all()
    footersectionOne = FootersectionOne.objects.all()
    footersectionTwo = FootersectionTwo.objects.all()
    footersectionThree = FootersectionThree.objects.all()
    footersectionFour = FootersectionFour.objects.all()
    startProjectContactAllDetail = StartProjectContactAllDetail.objects.all()
    if request.method == 'POST':
        form = ContactUs(request.POST)
        if form.is_valid():
                yn = form.cleaned_data['yourName']
                em = form.cleaned_data['email']
                cn = form.cleaned_data['companyname']
                bd = form.cleaned_data['budget']
                pn = form.cleaned_data['Phonenumber']
                sb = form.cleaned_data['Subject']
                me = form.cleaned_data['Message']
                reg = ContactsForm(yourName=yn,email=em,companyname=cn,budget=bd,Phonenumber=pn,Subject=sb,Message=me)
                reg.save()
                form = ContactUs()   
                return redirect ('/thankyou/')        
    else:
        form = ContactUs()
    if request.method == 'POST':
        subscribe = BlogEmail(request.POST)
        if subscribe.is_valid():
            em = subscribe.cleaned_data['email']
            sub = BlogSubscribe(email=em)
            sub.save()
            subscribe = BlogEmail() 
            return redirect ('/thankyou/')        

    else:
        subscribe = BlogEmail()
    return render (request,'app/blog.html',
        {   'form':form,
            'subscribe':subscribe,
            'headeritem': headeritem,
            'navLogo':navLogo,
            'blogtitle':blogtitle,
            'mainBlog':mainBlog,
            'blogLastSection':blogLastSection,
            'footersectionOne':footersectionOne,
            'footersectionTwo':footersectionTwo,
            'footersectionThree':footersectionThree,
            'footersectionFour':footersectionFour,
            'startProjectContactAllDetail':startProjectContactAllDetail,
            'favicon':favicon,
        })

def blogdetail (request,pk):
    favicon = Favicon.objects.all()
    blogdetail = MainBlog.objects.get(pk=pk)
    headeritem = Headeritem.objects.all()
    navLogo = NavLogo.objects.all()
    footersectionOne = FootersectionOne.objects.all()
    footersectionTwo = FootersectionTwo.objects.all()
    footersectionThree = FootersectionThree.objects.all()
    footersectionFour = FootersectionFour.objects.all()
    startProjectContactAllDetail = StartProjectContactAllDetail.objects.all()
    if request.method == 'POST':
        form = ContactUs (request.POST)
        if form.is_valid():
            yn = form.cleaned_data['yourName']
            em = form.cleaned_data['email']
            cn = form.cleaned_data['companyname']
            bd = form.cleaned_data['budget']
            pn = form.cleaned_data['Phonenumber']
            sb = form.cleaned_data['Subject']
            me = form.cleaned_data['Message']
            reg = ContactsForm(yourName=yn,email=em,companyname=cn,budget=bd,Phonenumber=pn,Subject=sb,Message=me)
            reg.save()
            form = ContactUs()  
            return redirect ('/thankyou/')        
    else:
        form = ContactUs()
    return render (request,'app/blogdetail.html',{
        'headeritem':headeritem,
        'favicon':favicon,
        'navLogo':navLogo,
        'blogdetail':blogdetail,
        'form':form,
        'footersectionOne':footersectionOne,
        'footersectionTwo':footersectionTwo,
        'footersectionThree':footersectionThree,
        'footersectionFour':footersectionFour,
        'startProjectContactAllDetail':startProjectContactAllDetail,
    })
# ==== blog Page Render ==== #


# ==== porfolio Page Render ==== #
def portfolio(request,data=None):
    favicon = Favicon.objects.all()
    headeritem = Headeritem.objects.all()
    navLogo = NavLogo.objects.all()
    if data == None:
        alldata = PorftolioCategorie.objects.all()
    elif data == 'graphicsdesign':
        alldata = PorftolioCategorie.objects.filter(category='GraphiceDesigning')
    elif data == 'webdevelopment':
        alldata = PorftolioCategorie.objects.filter(category='WebDevelopment')
    elif data == 'digitalmarketing':
        alldata = PorftolioCategorie.objects.filter(category='digitalmarketing')
    elif data == 'seosem':
        alldata = PorftolioCategorie.objects.filter(category='seo')
    elif data == 'contentwriting':
        alldata = PorftolioCategorie.objects.filter(category='contentwriting')
    elif data == 'videoediting':
        alldata = PorftolioCategorie.objects.filter(category='videoediting')
    videodata = PorftolioCategorie.objects.filter(category='videoediting')
    porftoliotitle = Porftoliotitle.objects.all()
    porftolioSection = PorftolioSection.objects.all()
    footersectionOne = FootersectionOne.objects.all()
    footersectionTwo = FootersectionTwo.objects.all()
    footersectionThree = FootersectionThree.objects.all()
    footersectionFour = FootersectionFour.objects.all()
    startProjectContactAllDetail = StartProjectContactAllDetail.objects.all()
    if request.method == 'POST':
        form = ContactUs(request.POST)
        if form.is_valid():
                yn = form.cleaned_data['yourName']
                em = form.cleaned_data['email']
                cn = form.cleaned_data['companyname']
                bd = form.cleaned_data['budget']
                pn = form.cleaned_data['Phonenumber']
                sb = form.cleaned_data['Subject']
                me = form.cleaned_data['Message']
                reg = ContactsForm(yourName=yn,email=em,companyname=cn,budget=bd,Phonenumber=pn,Subject=sb,Message=me)
                reg.save()
                form = ContactUs()   
                messages.success(request,"Thanks For Contacting Us We Will response Soon")   
                return redirect ('/thankyou/')        
    else:
        form = ContactUs()

    return render (request,'app/portfolio.html',
    {          
                'form':form,
                'favicon':favicon,
                'headeritem': headeritem,
                'navLogo':navLogo,
                'videodata':videodata,
                'porftoliotitle':porftoliotitle,
                'alldata':alldata,
                'porftolioSection':porftolioSection,
                'footersectionOne':footersectionOne,
                'footersectionTwo':footersectionTwo,
                'footersectionThree':footersectionThree,
                'footersectionFour':footersectionFour,
                'startProjectContactAllDetail':startProjectContactAllDetail,
        })

# ==== porfolio Page Render ==== #


# ==== privacy Page Render ==== #
def privacy(request):
    favicon = Favicon.objects.all()
    headeritem = Headeritem.objects.all()
    navLogo = NavLogo.objects.all()
    privacyBg = PrivacyBg.objects.all()
    privacyTitle = PrivacyTitle.objects.all()
    privacySectionOne = PrivacySectionOne.objects.all()
    privacySectionTwo = PrivacySectionTwo.objects.all()
    privacySectionthree = PrivacySectionthree.objects.all()
    privacySectionFour = PrivacySectionFour.objects.all()
    privacySectionfifth = PrivacySectionfifth.objects.all()
    privacySectionSixth = PrivacySectionSixth.objects.all()
    privacyLastsection = PrivacyLastsection.objects.all()
    footersectionOne = FootersectionOne.objects.all()
    footersectionTwo = FootersectionTwo.objects.all()
    footersectionThree = FootersectionThree.objects.all()
    footersectionFour = FootersectionFour.objects.all()
    startProjectContactAllDetail = StartProjectContactAllDetail.objects.all()
    if request.method == 'POST':
        form = ContactUs(request.POST)
        if form.is_valid():
                yn = form.cleaned_data['yourName']
                em = form.cleaned_data['email']
                cn = form.cleaned_data['companyname']
                bd = form.cleaned_data['budget']
                pn = form.cleaned_data['Phonenumber']
                sb = form.cleaned_data['Subject']
                me = form.cleaned_data['Message']
                reg = ContactsForm(yourName=yn,email=em,companyname=cn,budget=bd,Phonenumber=pn,Subject=sb,Message=me)
                reg.save()
                form = ContactUs()   
                messages.success(request,"Thanks For Contacting Us We Will response Soon")   
                return redirect ('/thankyou/')        
    else:
        form = ContactUs()
    return render (request,'app/privacy.html',{
        'favicon':favicon,
        'headeritem': headeritem,
        'navLogo':navLogo,
        'privacyBg':privacyBg,
        'privacyTitle':privacyTitle,
        'privacySectionOne':privacySectionOne,
        'privacySectionTwo':privacySectionTwo,
        'privacySectionthree':privacySectionthree,
        'privacySectionFour':privacySectionFour,
        'privacySectionfifth':privacySectionfifth,
        'privacySectionSixth':privacySectionSixth,
        'privacyLastsection':privacyLastsection,
        'form':form,
        'footersectionOne':footersectionOne,
        'footersectionTwo':footersectionTwo,
        'footersectionThree':footersectionThree,
        'footersectionFour':footersectionFour,
        'startProjectContactAllDetail':startProjectContactAllDetail,
    })

# ==== privacy Page Render ==== #
def termsandCondition(request):
    favicon = Favicon.objects.all()
    headeritem = Headeritem.objects.all()
    navLogo = NavLogo.objects.all()
    privacyBg = TermsAndConditionBg.objects.all()
    privacyTitle = TermsAndConditionTitle.objects.all()
    privacySectionOne = TermsAndConditionSectionOne.objects.all()
    privacySectionTwo = TermsAndConditionSectionTwo.objects.all()
    privacySectionthree = TermsAndConditionSectionthree.objects.all()
    privacySectionFour = TermsAndConditionSectionFour.objects.all()
    privacySectionfifth = TermsAndConditionSectionfifth.objects.all()
    privacySectionSixth = TermsAndConditionSectionSixth.objects.all()
    privacyLastsection = TermsAndConditionLastsection.objects.all()
    footersectionOne = FootersectionOne.objects.all()
    footersectionTwo = FootersectionTwo.objects.all()
    footersectionThree = FootersectionThree.objects.all()
    footersectionFour = FootersectionFour.objects.all()
    startProjectContactAllDetail = StartProjectContactAllDetail.objects.all()
    if request.method == 'POST':
        form = ContactUs(request.POST)
        if form.is_valid():
                yn = form.cleaned_data['yourName']
                em = form.cleaned_data['email']
                cn = form.cleaned_data['companyname']
                bd = form.cleaned_data['budget']
                pn = form.cleaned_data['Phonenumber']
                sb = form.cleaned_data['Subject']
                me = form.cleaned_data['Message']
                reg = ContactsForm(yourName=yn,email=em,companyname=cn,budget=bd,Phonenumber=pn,Subject=sb,Message=me)
                reg.save()
                form = ContactUs()   
                messages.success(request,"Thanks For Contacting Us We Will response Soon")   
                return redirect ('/thankyou/')        
    else:
        form = ContactUs()
    return render (request,'app/termsandCondition.html',{
        'favicon':favicon,
        'headeritem': headeritem,
        'navLogo':navLogo,
        'privacyBg':privacyBg,
        'privacyTitle':privacyTitle,
        'privacySectionOne':privacySectionOne,
        'privacySectionTwo':privacySectionTwo,
        'privacySectionthree':privacySectionthree,
        'privacySectionFour':privacySectionFour,
        'privacySectionfifth':privacySectionfifth,
        'privacySectionSixth':privacySectionSixth,
        'privacyLastsection':privacyLastsection,
        'form':form,
        'footersectionOne':footersectionOne,
        'footersectionTwo':footersectionTwo,
        'footersectionThree':footersectionThree,
        'footersectionFour':footersectionFour,
        'startProjectContactAllDetail':startProjectContactAllDetail,
    })

def faq(request):
    favicon = Favicon.objects.all()
    headeritem = Headeritem.objects.all()
    navLogo = NavLogo.objects.all()
    faqTitle = FaqTitle.objects.all()
    faqQuestion = FaqQuestion.objects.all()
    faqLeftQuestions = FaqLeftQuestions.objects.all()
    faqLastsection = FaqLastsection.objects.all()
    footersectionOne = FootersectionOne.objects.all()
    footersectionTwo = FootersectionTwo.objects.all()
    footersectionThree = FootersectionThree.objects.all()
    footersectionFour = FootersectionFour.objects.all()
    startProjectContactAllDetail = StartProjectContactAllDetail.objects.all()
    if request.method == 'POST':
        form = ContactUs(request.POST)
        if form.is_valid():
                yn = form.cleaned_data['yourName']
                em = form.cleaned_data['email']
                cn = form.cleaned_data['companyname']
                bd = form.cleaned_data['budget']
                pn = form.cleaned_data['Phonenumber']
                sb = form.cleaned_data['Subject']
                me = form.cleaned_data['Message']
                reg = ContactsForm(yourName=yn,email=em,companyname=cn,budget=bd,Phonenumber=pn,Subject=sb,Message=me)
                reg.save()
                form = ContactUs()   
                return redirect ('/thankyou/')        
    else:
        form = ContactUs()
    return render (request,'app/faq.html',{
        'favicon':favicon,
        'headeritem': headeritem,
        'navLogo':navLogo,
        'faqTitle':faqTitle,
        'faqQuestion':faqQuestion,
        'faqLeftQuestions':faqLeftQuestions,
        'faqLastsection':faqLastsection,
        'form':form,
        'footersectionOne':footersectionOne,
        'footersectionTwo':footersectionTwo,
        'footersectionThree':footersectionThree,
        'footersectionFour':footersectionFour,
        'startProjectContactAllDetail':startProjectContactAllDetail,
    })  

# ==== privacy Page Render ==== #

# ==== thanks Page Render ==== #

def thanks(request):
    favicon = Favicon.objects.all()
    headeritem = Headeritem.objects.all()
    navLogo = NavLogo.objects.all()
    thanks = Thanks.objects.all()
    footersectionOne = FootersectionOne.objects.all()
    footersectionTwo = FootersectionTwo.objects.all()
    footersectionThree = FootersectionThree.objects.all()
    footersectionFour = FootersectionFour.objects.all()
    startProjectContactAllDetail = StartProjectContactAllDetail.objects.all()
    return render(request,'app/thankyou.html',
    {   'favicon':favicon,
        'headeritem': headeritem,
        'thanks':thanks,
        'navLogo':navLogo,
        'footersectionOne':footersectionOne,
        'footersectionTwo':footersectionTwo,
        'footersectionThree':footersectionThree,
        'footersectionFour':footersectionFour,
        'startProjectContactAllDetail':startProjectContactAllDetail,
    })

# ==== thanks Page Render ==== #