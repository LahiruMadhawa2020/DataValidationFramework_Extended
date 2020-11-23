import pandas as pd
import pandas_profiling

class profilingBase:

    def __init__(self, dataframe_datasource):
        self.df = dataframe_datasource


    def sourcedataprofiling(self):
        # run the profile report
        profile = self.df.profile_report(title='Pandas Profiling Report')

        # save the report as html file
        profile.to_file(output_file="profiling_reports/pandas_profiling2c.html")

        # save the report as json file
        # profile.to_file(output_file="reports/pandas_profiling2b.json")