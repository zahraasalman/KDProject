<h1>Welcome to TouristiQ</h1>

This application is created to give the user information about any country or capital.

<h4>Installation:</h4>
<ul>
<li>Open the application folder in your terminal and execute the following command: 
<ul>
<code>pip install -U -r requirements.txt</code>
<li>This command installs all required modules to execute the application </li>
</li>
</ul>
<li>Before you can run the program, you need to insert a valid endpoint url at line 8 of queries.py.
<ul>
<li><code>endpoint = None</code> Replace <em>None</em> by your own endpoint url between quotation marks.</li>
<li>For example: <code>endpoint = "http://xxx.xxx.xxx.xxx:xxxx/repositories/YourRepositoryName"</code></li>
</li>
</ul>
<li>To run the application, in the location where the application files are located, execute the following command: </li>
<code>streamlit run index.py </code>
</ul>

<h4>Usage:</h4>

<h5>Enable custom coordinates</h5>
<p>This enables the user to insert custom coordinates, this could be usefull if the user wants to check a specific location that is not registered in the database or is not a country, city or capital.</p>

<h5>Filter by continent</h5>
<p>The user can select this option to filter the results by continent, this will narrow down the options the user has to all regions, countries and capitals of the chosen continent.</p>

<h5>Filter by region</h5>
<p>The user can select this option to filter the results by region, this is will narrow down the options the user has to all countries and capitals within the chosen region.</p>

<h5>Choose a country</h5>
<p>The user can select their desired country from a dropdown menu or type the name of the desired country and select it. This dropdown menu is always active and has to be used by the user to get a result.</p>

<h5>Filter by cities</h5>
<p>The user is able to filter by cities, this allows the user to pick any of the cities of the country that has been selected.</p>
<p>In the current version of the application, only the capital is available to the user.</p>

<h5>The map</h5>
<p>The map displays the location the user has selected, however, due to technical limitations of the framework this map is not interactable and purely acts as a mean to convey the location to the user and or allow the user to see the area of their desired location.</p>
