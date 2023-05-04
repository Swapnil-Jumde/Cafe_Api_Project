# Cafe_Api_Project

<body>
    <h1>Welcome to the Cafe API</h1>
<h2>End point: http://pythoninfotest.pythonanywhere.com</h2>
<table>
    <tr>
        <th>Route</th>
        <th>Parameters</th>
    </tr>
    <tr>
        <th><h3>/all</h3></th>
        <th><h4>Get All Cafes</h4></th>
    </tr>
    <tr>
        <th><h3>/random</h3></th>
        <th><h4>Get Random Cafe</h4></th>
    </tr>
    <tr>
        <th><h3>/add</h3></th>
        <th><h4>
        name,<br>
        map_url,<br>
        img_url,<br>
        location,<br>
        has_sockets,<br>
        has_toilet,<br>
        has_wifi,<br>
        can_take_calls,<br>
        seats,<br>
        coffee_price<br>
    [parameters required]</h4>
</th>
    </tr>
    <tr>
        <th><h3>/search</h3></th>
        <th><h4>loc='location' [required]</h4><p> eg: http://pythoninfotest.pythonanywhere.com/search?loc=London </p></th>
    </tr>
    <tr>
        <th><h3>/update-price</h3></th>
        <th><h4>cafe_id  [required]</h4><p>http://pythoninfotest.pythonanywhere.com/update-price/22?new-price=$275</p></th>
    </tr>
    <tr>
        <th><h3>/report-closed</h3></th>
        <th><h4>cafe_id [required for delete]</h4><p>http://pythoninfotest.pythonanywhere.com/report-closed/22?api-key=YourApiKey</p></th>
    </tr>
</table>
<br>
<br>
<h2 style="text-align:center;">Thank You</h2>
<br>
<br>
<br>
</body>
</html>
