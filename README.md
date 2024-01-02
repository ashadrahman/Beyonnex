# Beyonnex QA Tech Challenge

<hr>
This project is to automate the complete shopping of the web app 'Weather Shopper' (http://weathershopper.pythonanywhere.com/) from opening the window to the payment with the help of selenium and python and Docker. It runs in headless mode, but it can be run in headful mode too by removing the headless option in the driver code.
<br>Also, the CI pipeline is created in github actions. The docker build and the tests will run every time if a new commit or code push happens to this repo.

<br><strong>Key points according to which this project works</strong>
<ul>
 <li> It uses the test website: https://weathershopper.pythonanywhere.com/ </li>
  <li> At first it choose the temperature according to which it will go to the season whether it needs moisturizers or sunscreens. If the temperature is below 19 degrees it choose moisturizers and if the temperature is above 34 degrees it choose sunscreens. </li>
  <li> At sunscreens it will take least priced SPF-50 and SPF-30 products and add to the cart</li>
   <li> At Moisturizers it will take least priced ALOE and ALMOND products and add to the cart</li>
   <li> Then it will go to stripe payment and fills dummy/test account details and clicks over pay after which it will show a page showing payment successful</li>
 </ul>
 <br><strong> Tips to use:</strong>
 <br>Install python3 into your system<br>
<br>Install selenium into your system<br>
    <pre>pip3 install selenium</pre>
execute the app.py
<pre>python3 app.py</pre>
<br><strong>Using Docker to run:</strong>
<br>Install docker on your local machine. Then goto to the project folder location and run this command:<br>
  <pre>docker build -t BUILD_NAME .</pre>
  <pre>docker run BUILD_NAME </pre>
 <hr><hr>

