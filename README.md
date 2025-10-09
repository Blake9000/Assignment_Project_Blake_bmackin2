This project aims to create a service status dashboard for the servers I already host (Apache Webserver, ESXI, Minecraft, Pterodactyl). This will allow me to view their status and logs from a centralized locations

![erd.png](docs/ERD/erd.png) 

Currently, I have added a login screen, log view screen, and dashboard screen.
The login screen is currently static, as I have not learned how to properly manage users yet.
The log view screen currently just shows all the logs that are in the db.
The dashboard also shows all the services and their status (UP or DOWN)

I have added detail views for both logs and services. This allows you to click on a log or service and view all details related to them.
I have added a search bar to the log viewer. This allows you to search all aspects of the log (timestamp, message, level, etc.).
I have also refactored links to be dynamic and made some small visual changes.

In A6, I added aggregations. Since I already created a search bar last week, it still remains. The aggregation shows the total logs and the number of unique log types contained within.