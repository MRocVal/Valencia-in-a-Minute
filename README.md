![](encabezado.jpg)

# Valencia In A Minute

Welcome to Valencia In A Minute, an application designed to provide real-time updates and precise information on public transportation in Valencia, including the metro, buses, and Valenbisi bikes. This tool helps you optimize your travel time and provides a seamless commuting experience.

## Features

-   **Real-Time Updates**: Get instant information about metro and bus arrivals and departures.
-   **Interactive Maps**: Explore interactive maps for metro lines and EMT bus stops.
-   **ValenBisi Route Duration**: Calculate the travel time between Valenbisi bike stations to ensure you don't exceed your rental time.

## Installation

1.  Clone the repository:

    ```{bash}
    git clone https://github.com/your-repo/valencia-in-a-minute.git
    ```

2.  Navigate to the project directory

    ```{bash}
    cd valencia-in-a-minute
    ```

3.  Install the required dependencies:

    ```{bash}
    pip install -r requirements.txt
    ```

    ### Usage

    To run the application, use the following command:

    ```{bash}
    streamlit run Valencia_Al_Minuto.py
    ```

    ## 

    Pages

### Home

Provides an overview of the application, including its features and a contact section for any suggestions or inquiries.

### MetroValencia Schedule

Check the next arrivals and departures at your selected metro station.

-   **Enter the Station Name**: You can try entering benimac and pressing enter to see the results.
-   **Select a Station**: Choose from the filtered list of stations to get updated information on the next trains.

### Interactive Map

Explore the interactive map of metro lines.

-   **Select Metro Lines**: Choose the lines you are interested in and see their geographical distribution.

### EMT Schedules

Quickly check the next arrivals at your selected bus stop.

-   Enter the name or number of the stop: Filter the list of stops to find your desired stop.
-   **Select a Stop**: Choose a stop to get updated information on the upcoming buses.

### EMT Map

Explore the interactive map of EMT bus stops in Valencia.

-   **Filter stops by name**: Find stops by entering a name or part of a name.
-   **Select Stops**: Choose from the list of filtered stops to see their locations on the map.

### ValenBisi Route Duration

Calculate the travel time from one Valenbisi stop to another.

-   **Select two stops**: Use the search fields to find and select two Valenbisi stops.

-   **Calculate Route**: Click the button to calculate the route and see the estimated time. If you click on the bicycle icon on the map, it will display the number of bikes parked and the available spaces to leave them.

### Contact

For any suggestions or inquiries, please send an email to [mrocval\@etsinf.upv.es](mailto:mrocval@etsinf.upv.es).
