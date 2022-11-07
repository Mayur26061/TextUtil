from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'home.html')
def contact(request):
    return render(request,'contact.html')
def analyze(request):
    txt=str(request.POST.get('text','default'))    
    chkrem=request.POST.get('rpun','off')
    chkupp=request.POST.get('upp','off')
    chknew=request.POST.get('newline','off')
    chkspc=request.POST.get('spcrmv','off')
    chk=request.POST.get('charcount','off')
    count=0
    bol=False
    para={}
    analyzed=txt 
    if chkrem=='on':
        bol=True
        pun='''!()-[]}{;:'"\,<>./?@#$%^&*_~'''
        txt=analyzed
        analyzed=""
        for ch in txt:
            if ch not in pun:
                analyzed=analyzed+ch

    if chkupp=='on':
        bol=True
        analyzed=analyzed.upper()
    
    if chknew=='on':
        bol=True
        ls =analyzed.split('\r\n')
        analyzed=" ".join(ls)
        
       
    if chkspc=='on':
        bol=True
        ck=""
        for ind,char in enumerate(analyzed):
            if not (analyzed[ind]==" " and analyzed[ind+1]==" "):
                ck=ck+char
        analyzed=ck
    if chk=='on':
        bol=True
        count=len(analyzed)
        x="Size of text is "+str(count)
        para['count']=x
    if not bol:
        return HttpResponse("error")
    para['analyzed_text']=analyzed
    para['name']='Analyzed Text'
    return render(request,'analy.html',para)         

