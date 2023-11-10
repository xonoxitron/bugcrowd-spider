# Author: Matteo (xonoxitron) Pisani
# Description: Extracts all programs with payments from https://bugcrowd.com/programs, for each programme obtained extracts the targets in scope and the program url
# Usage: python3 bugcrowd-spider.py

import requests
import json

# Define target
target = "https://bugcrowd.com"

# Define the base URL with the pagination argument
base_url = target + "/programs.json?vdp[]=false&sort[]=promoted-desc&page[]="

# Define the starting page number
start_page = 1

# Define the output json to be serialized
json_output = {"programs": []}

while True:
    # Create the URL with the current page number
    url = f"{base_url}{start_page}"

    try:
        # Make an HTTP GET request to fetch the JSON data
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON data
            json_data = response.json()

            # Reached the end
            if len(json_data["programs"]) == 0:
                break

            # Extrapolating JSON program names
            for program in json_data["programs"]:
                # Getting program name
                program_name = program["name"]

                # Getting program url
                program_url = program["program_url"]

                print(f"Fetching {program_name} targets from {program_url}")

                # Make an HTTP GET request to fetch the nested JSON data
                nested_response = requests.get(
                    f"{target}{program_url}/target_groups.json"
                )

                # Check if the nested request was successful (status code 200)
                if nested_response.status_code == 200:
                    # Parsing the nested JSON data
                    nested_json_data = nested_response.json()

                    # Creating rewards variable
                    rewards = []
                    # No groups
                    if len(nested_json_data["groups"]) == 0:
                        break

                    # Parsing groups
                    for group in nested_json_data["groups"]:
                        # Filter group by "In-scope"
                        if group["in_scope"] == True:
                            # No reward range
                            if len(group["reward_range"]) == 0:
                                continue

                            # Printing rewards
                            rewards.append(group["reward_range"])

                    # Append program entry
                    json_output["programs"].append(
                        {
                            "name": program_name,
                            "url": f"{target}{program_url}",
                            "rewards": rewards,
                        }
                    )

            # Increment the page number for the next iteration
            start_page += 1
        else:
            print(
                f"Request for page {start_page} failed with status code {response.status_code}"
            )
            break  # Exit the loop if the request fails

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from page {start_page}: {e}")
        break  # Exit the loop if an exception occurs

# Writing output json to file
with open("bugcrowd-programs.json", "w") as write:
    json.dump(json_output, write)
print("Done.")

# This loop will continue until an exception occurs during the request.
