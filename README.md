<h1>Data-Integration-template</h1>
This project was created in order for QC(quality control) labs or students to easily keep track of their Products. It will allow them to keep track of certain chemical information about their products as well as update them using an easy to use google sheets API. this example has been made to check different type of olive oils.

<h2>Site Goals</h2>
<p>This is a simple application to give user a template to quickly modify and quickly keep track of their data and do integration on them</p>
<h2>Target Audience</h2>
<p>students or QC labs to have an user friendly way to do manipilation and keep track of the chemical data of their products</p>
<h2>User Stories</h2>

<li>As a User, I would like to be able to easily input my data in a well know 
environment which requires no/minimal training to use</li>
<li>As a User, I would like to be able to check all the data steps because this could be important in case of audit or check for mistakes</li>
<li>As a User, I would like to be able to to visualize my acquired Data</li>
<li>As a User, I would like to be able to to visualize my acquired Data to see certain trends</li>

<img src="docs/readme/Navigation.jpg" alt="navigation">

<h3>Features Planned</h3>

<li>Simple easy to use application using a familiar environment</li>
<li>Simple storage of the data</li>
<li>Visualization of the data</li>
<li>data manipulation to give more information to the user</li>
<li>looking for trends of the last data set to see changes</li>
<h2>Structure</h2>
<h3>USER STORY</h3>
<ol>
<li>As a User, I would like to be able to easily input my data in a well know 
environment which requires no/minimal training to use</li>

</ol>
<img src="docs/readme/footer.jpg" alt="footer">
<h3>IMPLEMENTATION</h3>
<li>API to google sheets</li>
<p>excel is a familiar environment for many user so it will be an ideal place to do this.</p>
<li>The user will put the data as required in this application in the google sheets Raw_Data file</li><a href="">link</a>
<p>in case a wrong data has been imported they will get a notification to alter it and the program won't run</p>
<li>when the data has been input they just need to press "x" to run the program</li>


<h3>USER STORY</h3>
<p>As a User, I would like to be able to to visualize my acquired Data</p>
<h3>IMPLEMENTATION</h3>
<li>plotting of the data that has been added to google sheets file using plotext library</li>
<p>once the programme starts running after the data check it will plot the data </p>
<img src="docs/readme/footer.jpg" alt="footer">
<h3>USER STORY</h3>
<li>data manipulation to give more information to the user</li>
<li>As a User, I would like to be able to check all the data steps because this could be important in case of audit or check for mistakes</li>
<p>spectrum of Olive oil</p>
<img src="docs/readme/footer.jpg" alt="footer">
<h3>IMPLEMENTATION</h3>
<li>the numpy libary is has been used to integrate the data using trap integration</li>
<p>the Data was tested using https://www.integral-calculator.com/ and integration by hand. The function Test-Data as used</p>
<li>Integration of certain chemical vibrations to determine the presence of oxygenated groups and the branching of the olive oils</li>
<p>The integrations borders can be changed in the top of the program for flexibility</p>
<li>Afterwards the integrated data is added to the Integrated_Data sheet for to see the actual integrated values</li>

<p>this is very important to check your data and for audit purposes because the all steps can be traced back</p>

<li>Integration of certain chemical vibrations to determine the presence of oxygenated groups and the branhing of the olive oils</li>

 <img src="docs/readme/landingpage.jpg" alt="picture of the landingpage of the website">
<p>explains why CSV files are often used. Secondly how to structure them for usage</p>
<img src="docs/readme/CreationCSV.jpg" alt="picture of why CSV as data source">
<p>a shortcut to start creating charts</p>
<img src="docs/readme/chart-generator-link.jpg" alt="short cut button">
<h3>Website information on 'Chart Types'</h3>
<p>It will explain which chart types are good for which applications. (barchart,piechart, lineplot and scatterplot) </p>

<img src="docs/readme/Charttype.jpg" alt="Picture chartype page">


<h3>Structure</h3>
<p>this page contains a form to convert your CSV-file into a charts and choosing the type of chart you would like</p>
<img src="docs/readme/ChartForm.jpg" alt="chart form">

<p>this shows the 2 buttons how to download your made charts and make new one by making free the canvas</p>
<img src="docs/readme/DownloadDestroy.jpg" alt="picture of dowload and destroy button">

<h3>404 page</h3>
an error page has been developed in case links are missing or wrong. it has a button that will bring you back to the landing page.
<img src="docs/readme/404.jpg" alt="picture of 404 page">
<h3>Features Left to Implement</h3>
<ul> 
<li>Changing favicon of the scatterplot</li>
<li>making it possible to have line chart that have more axes</li>
<li>increase the different types of charts can be generated</li>
</ul>

<h3>Existing Features</h3>
<ul>
<li>Responsive design</li>
<li>navigation menu</li>
<li>Hidden interactive sections on Chart Type page</li>
<li>information about different type of charts</li>
<li>CSV reader</li>
<li>Chart renderer</li>
<li>Page animations</li>
<li>check datafile for NaN values</li>
<li>download the created chart</li>
<li>404 page</li>
</ul>



<h3>Design</h3>
<h4>website design</h4>
<p>Home page</p>
<img src="docs/readme/landingpagewireframe.jpg" alt="design of the landing page">
<p>Chart Type</p>
<img src="docs/readme/ChartTypeWireframe.jpg" alt="design of the charttype page">
<p>Chart Generator</p>
<img src="docs/readme/ChartGeneratorWireframe.jpg" alt="design of the Chart Generator page">

<h4>phone design</h4>
<p>Home page</p>
<img src="docs/readme/andriodHomePage.jpg" alt="design of the landing page">
<p>Chart Type</p>
<img src="docs/readme/AndriodChartType.jpg" alt="design of the Chart Type page">
<p>Chart Generator</p>
<img src="docs/readme/WireFrameChartGenerator.jpg" alt="design of Chart Generator page">

<h3>Technologies</h3>
<ul>
<li>HTML</li>
<p>The structure of the Website was developed using HTML as the main language.</p>
<li>CSS</li>
<p>The Website was styled using custom CSS in an external file.</p>
<li>Javascript</li>
<p>The chart generator and chart type animition were created using JavaScript in an external file.</p>
<li>Visual Studio Code</li>
<p>The website was developed using Visual Studio Code IDE</p>
<li>GitHub </li>
<p>Source code is hosted on GitHub and delpoyed using Git Pages.</p>
<li>Git </li>
<p>Used to commit and push code during the development opf the Website</p>
<li>Font Awesome</li>
<p>Icons obtained from https://fontawesome.com/ were used as the Social media links in the footer section.
</p>
<li>balsamiq</li>
<p>wireframes were created using balsamiq from https://balsamiq.com/wireframes/desktop/#</p>
<li>Favicon.io</li>
<p>favicon files were created at https://favicon.io/favicon-converter/</p>
<img src="docs/readme/favicon.jpg" alt="Picture of the favicon icon">
<li>Chart.JS</li>
<p>Graph were created using chart.js libaries https://www.chartjs.org/docs/latest/</p>
</ul>
<h3>Testing</h3>
<h4>Responsiveness</h4>
<p>All pages were tested to ensure responsiveness on screen sizes from 500px and upwards as defined in WCAG 2.1 Reflow criteria for responsive design on Chrome, Edge, Firefox and Opera browsers.</p>

<p>Steps to test:</p>
<ul>
<li>Open browser and navigate to Data Visualazation</li>
<li>Open the developer tools (right click and inspect)</li>
<li>Set to responsive and decrease width to 320px</li>
<li>Set the zoom to 50%</li>
<li>Click and drag the responsive window to maximum width</li>
</ul>
<p>Expected:</p>

<p>Website is responsive on all screen sizes and no images are pixelated or stretched. No horizontal scroll is present. No elements overlap.(chrome,edge) </p>

<p>Actual:</p>

<p>Website behaved as expected.</p>

<p>Website was also opened on the following devices and no responsive issues were observed</p>
<ul>
<li>iPhoneSE</li>
<li>Samsung Galaxy S8</li>
<li>iPad Air</li>
<li>Samsung Galaxy A51/71</li>
<li>Nest Hub Max</li>
</ul>

<h4>Testing was focused to ensure the following criteria were met:</h4>

Color contrasts meet a minimum ratio as specified in WCAG 2.1 Contrast Guidelines
Heading levels are not missed or skipped to ensure the importance of content is relayed correctly to the end user
All content is contained within landmarks to ensure ease of use for assistive technology, allowing the user to navigate by page regions
All not textual content had alternative text or titles so descriptions are read out to screen readers
HTML page lang attribute has been set
Aria properties have been implemented correctly
WCAG 2.1 Coding best practices being followed
Manual tests were also performed to ensure the website was accessible as possible and an accessibility issue was identified.

<h4>Chart Funtionalities</h4>
<h5>Chart Generation Scatterplot</h5>
<p>Steps to test:</p>

<ul>

<li>Open browser and navigate to Data Visualazation</li>
<li>Navigate to the Chart Generator</li>
<li>Upload (TestingCSVExcelScatterplot.csv or TestingCSVWordpadScatterplot.txt)</li>
<li>Type in header, X-axes, Y-axes</li>
<li>Select a type of Chart</li>
<li>Click the Generate Button</li>
</ul>

<p>Expected:</p>

<p>Chart is being generated </p>

<p>Actual:</p>

<p>Chart is being generated</p>

<h5>Chart Delimiter</h5>
<p>Steps to test:</p>

<ul>

<li>Open browser and navigate to Data Visualazation</li>
<li>Navigate to the Chart Generator</li>
<li>Upload (TestingCSVdelimtercomma.txt)</li>
<li>Select the comma(,) delimiter</li>
<li>Type in header, X-axes, Y-axes</li>
<li>Select a type of Scatterplot</li>
<li>Click the Generate Button</li>
</ul>

<p>Expected:</p>
<p>Chart is being generated </p>

<p>Actual:</p>

<p>Chart is being generated</p>

<h5>Data pop up</h5>
<p>Steps to test:</p>

<ul>

<li>Open browser and navigate to Data Visualazation</li>
<li>Navigate to the Chart Generator</li>
<li>Upload (badCSVfile.csv)</li>
<li>Select the comma(;) delimiter</li>
<li>Type in header, X-axes, Y-axes</li>
<li>Select a type of Scatterplot</li>
<li>Click the Generate Button</li>
</ul>

<p>Expected:</p>
<p>pop up</p>
<img src="docs/readme/POPUP.jpg" alt="pop up alert" >
<p>Actual:</p>
<img src="docs/readme/POPUP.jpg" alt="pop up alert" >


<h5>Chart Generation(Barchart, Piechart and Lineplot)</h5>
<p>Steps to test:</p>

<ul>

<li>Open browser and navigate to Data Visualazation</li>
<li>Navigate to the Chart Generator</li>
<li>Upload (TestingCSVExcel.csv or TestingCSVWordpad.txt)</li>
<li>Type in header, X-axes, Y-axes</li>
<li>Select a type of Chart</li>
<li>Click the Generate Button</li>
</ul>

<p>Expected:</p>

<p>Chart is being generated with titel and axes titles</p>

<p>Actual:</p>

<p>Chart is being generated with titel and axes titles</p>

<h5>Download and Discard buttons</h5>
<p>Steps to test:</p>

<ul>

<li>First Generate a chart(see Chart Generation)</li>
<li>Click the Chart Discard button</li>
<li>Click the Generate Button</li>
<li>Click the Dowload Button </li>
</ul>

<p>Expected:</p>

<p>Chart will be present afterwards it will be remove from the canvas using the Chart discard button. You will regenerate the Chart. now the dowload button is clicked and the downloaded as a PNG</p>

<p>Actual:</p>

<p>Chart is being Discarded. Regenerated followed by a download as a PNG</p>

<h4>Chart Types</h4>
<h5>Chart Type buttons</h5>
<p>Steps to test:</p>

<ul>

<li>Open browser and navigate to Data Visualazation</li>
<li>Navigate to the Chart Types</li>
<li>Click on the BarChart button</li>
<li>Click on the LinePlot button</li>
<li>Click on the PieChart button</li>
<li>Click on the Scatterplot button</li>
</ul>

<p>Expected:</p>

<p>the text changes in respect to chart type that has been choses by clicking the button</p>

<p>Actual:</p>

<p>the text changes in respect to chart type that has been choses by clicking the button</p>

<h3>lighthouse testing</h3>
<img src="docs/readme/lighthouse.jpg" alt="lighthouse report website" width=40% height=60px>

<h3>Functional Testing</h3>

<h4>Navigation Links</h4>

Testing was performed to ensure all navigation links on the respective pages, navigated to the correct pages as per design. This was done by clicking on the navigation links on each page.

Navigation Link	Page to Load
<p>Home Page	 to       index.html</p>
<p>Chart Types    to      graph.html</p>
<p>Chart Generator	 to   generator.html</p>

Links on all pages navigated to the correct pages as exptected.

<h4>Footer Social Media Icons / Links</h4>

Testing was performed on the Font Awesome Social Media icons in the footer to ensure that each one opened in a new tab.

Each item opened a new tab when clicked as expected.


<h4>Validator Testing</h4>
<ul>
<li>HTML</li>
<p>No errors were returned when passing through the official W3C validator</p>

index HTML Validator Results

<img src="docs/readme/htmlvalidatorindex.jpg" alt="Valid html!" />

graph HTML Validator Results

<img src="docs/readme/htmlvalidatorgraph.jpg" alt="Valid html!" />

generator HTML Validator Results

<img src="docs/readme/htmlvalidatorgenerator.jpg" alt="Valid html!" />

404 HTML Validator Results
<img src="docs/readme/htmlvalidator404.jpg" alt="Valid html!" />


<li>CSS</li>
<p>No errors were found when passing through the official (Jigsaw) validator</p>
CSS Validator Results

<p>stylesheet CSS Validator Results</p>
<p>
    <a href="https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Ffrangidha.github.io%2FData-Visualisation-%2Findex.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss-blue"
            alt="Valid CSS!" />
    </a>
</p>

<p>stylesheetgraph CSS Validator Results</p>
<p>
    <a href="https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Ffrangidha.github.io%2FData-Visualisation-%2Fgraph.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss-blue"
            alt="Valid CSS!" />
    </a>
</p>


<p>stylesheetgenerator CSS Validator Results</p>
<p>
    <a href="https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Ffrangidha.github.io%2FData-Visualisation-%2Fgenerator.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss-blue"
            alt="Valid CSS!" />
    </a>
</p>

<li>Javascript</li>
<p>No errors were returned when passing through the <a href="https://jshint.com/" target="_blank">JShint validator</a>

<p>A warning appeared for one function as an unused variable but the function is being used directly as an onkeyup event on the Discard Chart and Dowload events.</p>
<p>variables are undefienied because the user will define them.</p>
graph.js
<div>

<img src="docs/readme/Graph warning.jpg" alt="JShint warnings of graph.js" ></div>
script.js
<div>

<img src="docs/readme/Generator warning.jpg" alt="JShint warnings of script.js" >
</div>

</ul>
<h3>Bugs and fixes</h3>
problem with the values of the data integration due to . seperator for values bigger then a thousand. a fix was impleted so the . seperator was removed.


<h3>unfixed bugs</h3>
Due to the problem of using the API the loop function is limited to maximum of 3 values per time due to the limit of the measurements. change to the code to have less problem with the quota of the API

<h3>Deployment</h3>
<h4>Version Control</h4>
The site was created using the Visual Studio code editor and pushed to github to the remote repository ‘history’.

The following git commands were used throughout development to push code to the remote repo:

git add <file> - This command was used to add the file(s) to the staging area before they are committed.

git commit -m “commit message” - This command was used to commit changes to the local repository queue ready for the final step.

git push - This command was used to push all committed code to the remote repository on github.

<h4>Heroku Deployment</h4>
The below steps were followed to deploy this project to Heroku:
<ul>
<li>Go to Heroku and click "New" to create a new app.</li>
<li>Choose an app name and region region, click "Create app".</li>
<li>Go to "Settings" and navigate to Config Vars. Add the following config variables:</li>
<li>PORT : 8000</li>
<li>Navigate to Buildpacks and add buildpacks for Python and NodeJS (in that order).</li>
<li>Navigate to "Deploy". Set the deployment method to Github and enter repository name and connect.</li>
<li>Scroll down to Manual Deploy, select "main" branch and click "Deploy Branch".</li>
<li>The app will now be deployed to heroku</li>
<li><a href="https://www.golinuxcloud.com/javascript-csv-to-array/#:~:text=Method%2D1%3A%20Use%20split()%20method%20to%20convert%20CSV%20to%20Array,-Before%20we%20go&text=split()%20%2C%20and%20it%20takes,typically%20a%20comma%20(%20%2C%20)." target="_blank">ToDolink</a></li>
 </ul>

<h4>Clone Locally</h4>
<ul>
<li>Open IDE of choice and type the following into the terminal:</li>
<li>git clone https://github.com/Gareth-McGirr/motorcycle-rental-management.git</li>
<li>Project will now be cloned locally.</li>
<li>Open your IDE of choice (git must be installed for the next steps)</li>
<li>Type git clone copied-git-url into the IDE terminal</li>
<li>The project will now of been cloned on your local machine for use.</li>
</ul>
<h3>Credits</h3>
<h5>StackOverflow</h5>
<p>was used for certain bug fixes which were encounterd during the programming process </p>
<h5>Code insitute</h5>
<p>the code insitute curriculum was used to develop the entire application. Mainly the love-sandwiches project was great inspiration to find out how to connect the file to google sheets.<a href="github.com/Code-Institute-Solutions/love-sandwiches">link</a></p>
