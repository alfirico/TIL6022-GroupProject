# TIL6022-GroupProject

This repository contains the code and data analysis related to our group project for the TIL6022 course at TU Delft.

*Members:* Alfi Rico Davey, Artemis Kalapouti, Bo de Man, Mariana Julietti Pelozo, Thomas Mennill

*Student numbers:* 6304419, 6223087, 5040213, 6304761, 6210139

  

## Repository structure

  

T## Repository Structure

  

-  **data/**

	-  **commute-data/**

		-  **final-commute-data/** # Processed commute data

		-  **raw_data/** # Raw commute data files

	-  **traffic-jam-data/**

		-  **filtered_data/** # Filtered traffic data for analysis

		-  **raw_data/** # Raw traffic data files

-  **images/** # Visualizations and figures used in the report

-  **project-proposal/** # Proposal documents

-  **scripts/** # Python scripts used for data processing and analysis

	-  **analysis/**

		-  **commute-analysis/**

			-  `cartrip_commute_analysis.py` # Creates the car trips graph

			-  `commute_analysis.py` # Creates the total trips graph

		-  **traffic-analysis/**

			-  `heaviness_processing_and_graph.py` # Creates the heaviness graph

	-  **data-processing/**

		-  `Filter_and_translate_traffic_jam_data.py` # Filters the traffic jam data

		-  `Filter_commuting_data.py` # Combines all the commuting data files 

-  `Report.ipynb` # Jupyter notebook with the final analysis report

-  `README.md` 