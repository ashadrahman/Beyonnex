# Beyonnex Tech Challenge

<hr>
This project is to automate the complete shopping of the web app 'Weather Shopper' (http://weathershopper.pythonanywhere.com/) from opening the window to the payment with the help of selenium and python and Docker. It runs in headless mode, but it can be run gui mode too by removing the headless option in the driver code.

<br><strong>Key points according to which this project works</strong>
<ul>
 <li> It uses the test website: https://weathershopper.pythonanywhere.com/ </li>
  <li> At first it choose the temperature according to which it will go to the season whether it needs moisturizers or sunscreens. If the temperature is below 19 degrees it choose moisturizers and if the temperature is above 34 degrees it choose sunscreens. </li>
  <li> At sunscreens it will take least priced SPF-50 and SPF-30 products and add to the cart</li>
   <li> At Moisturizers it will take least priced ALOE and ALMOND products and add to the cart</li>
   <li> Then it will go to stripe payment and fills dummy/test account details and clicks over pay which will show a page showing payment successful</li>
 </ul>
 <br><strong> Tips to use:</strong>
<br>Install selenium into your system<br>
    <pre>pip3 install selenium</pre>
provide executable permission to driver_installer
  <pre>chmod -x driver_installer.sh</pre>
   execute the driver_installer
   <pre>./driver_installer.sh</pre>
If you have firefox browser then it's ok, if you have any other browser like chrome just change the line "browser = webdriver.Firefox()" in app.py with your browser line, like for chrome its:
<pre>"browser = webdriver.Chrome()"</pre>
execute the app.py
<pre>python3 app.py</pre>
<br><strong>Using Docker to run:</strong>
<br>Goto to the installed directory and run this command:<br>
  <pre>docker build -t <anybuildname> .</pre>
  <pre>docker run -it <anybuildname> </pre>
 <hr><hr>

