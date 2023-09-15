Location Tracking Application
------------------------------

Setup
-----
1. run the setup.bat file
2. within that virtual environment, open two terminals
    a) Run the GPS_data_producer.py script, which will take the user input in console

        python gps_data_producer.py

    
    b) run the flask application, which is the subscriber and it visualizes the GPS coordinates in web application

        python app.py


web application link
----------------------
    After setup, use console of gps_data_producer.py script to input GPS data

    To visualize the web app, click below link
    
        http://127.0.0.1:5000/


enhancements
------------
    - Instead of reloading the web page after each input, in console, It can be enhanced to automatically reload the webpage.after every user input.

    