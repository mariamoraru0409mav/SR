# Healthcare No-Shows Recombee Uploader

This project uploads healthcare appointment data from a CSV file to the Recombee platform. It defines item properties relevant to healthcare appointments and sends batch data to Recombee for further analysis or recommendation tasks.

## Features

- Defines item properties such as age, gender, medical conditions, and appointment details.
- Reads appointment data from a CSV file.
- Uploads data to Recombee using batch requests.


## CSV Format

The CSV file (`healthcare_noshows.csv`) should have the following columns:
1. to identify the appointment:
- appointmentId,
- appointmentDay.
2. to identify the patient:
- age,
- alcoholism,
- diabetes,
- gender,
- handicap,
- hipertension,
- neighbourhood,
- patientId,
- scholarship,
- showed_up. 

## Usage

1. Place your `healthcare_noshows.csv` file in the project directory.
2. Update Recombee credentials in `main.py` if needed.
3. Run the script:

```sh
python3 main.py
```

The script will:
- Add item properties to Recombee.
- Upload all appointment records from the CSV file.
