# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "2ccca003-4d0d-45fa-bee7-a73296ebce16",
# META       "default_lakehouse_name": "Shortcut_Exercise",
# META       "default_lakehouse_workspace_id": "865bdcba-9e33-46d5-9890-9770083bab15",
# META       "known_lakehouses": [
# META         {
# META           "id": "2ccca003-4d0d-45fa-bee7-a73296ebce16"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

df = spark.sql("SELECT * FROM Shortcut_Exercise.dbo.dimension_customer LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
