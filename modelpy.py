import pickle
import pandas as pd


class Model:

    def __init__(self):
        self.last_Date = pd.to_datetime("2017-12-30")
        file = open('./arima_time_series_forecasting.pkl', 'rb')
        self.model = pickle.load(file)

    def predict_on_days(self, ndays):
        period_list = []
        target_list = []
        output_data_dict = {}
        to_date = self.last_Date + pd.DateOffset(days=ndays)
        self.res = self.model.get_prediction(start=pd.to_datetime(self.last_Date), end=pd.to_datetime(to_date),
                                             dynamic=False)
        df = pd.DataFrame(self.res.predicted_mean)
        df.to_csv("result.csv")
        df["date"] = pd.to_datetime(df.index)
        df["date"] = df["date"].dt.strftime("%Y-%m-%d")
        df.reset_index(inplace=True)

        for i in range(len(df)):
            period_list.append(df.loc[i, "date"])
            target_list.append(df.loc[i, "predicted_mean"])

        output_data_dict["period"] = period_list
        output_data_dict["target"] = target_list

        return output_data_dict

    def predict_on_months(self, nmonths):
        output_data_dict = {}
        period_list = []
        target_list = []
        to_date = self.last_Date + pd.DateOffset(months=nmonths)
        self.res = self.model.get_prediction(start=pd.to_datetime(self.last_Date), end=pd.to_datetime(to_date),
                                             dynamic=False)
        df = pd.DataFrame(self.res.predicted_mean)
        df.to_csv("result.csv")
        df["date"] = pd.to_datetime(df.index)
        df["date"] = df["date"].dt.strftime("%Y-%m-%d")
        df.reset_index(inplace=True)
        for i in range(len(df)):
            period_list.append(df.loc[i, "date"])
            target_list.append(df.loc[i, "predicted_mean"])

        output_data_dict["period"] = period_list
        output_data_dict["target"] = target_list

        return output_data_dict

    def predict_on_years(self, nyears):
        output_data_dict = {}
        period_list = []
        target_list = []
        to_date = self.last_Date + pd.DateOffset(years=nyears)
        self.res = self.model.get_prediction(start=pd.to_datetime(self.last_Date), end=pd.to_datetime(to_date),
                                             dynamic=False)
        df = pd.DataFrame(self.res.predicted_mean)
        df.to_csv("result.csv")
        df["date"] = pd.to_datetime(df.index)
        df["date"] = df["date"].dt.strftime("%Y-%m-%d")
        df.reset_index(inplace=True)
        for i in range(len(df)):
            period_list.append(df.loc[i, "date"])
            target_list.append(df.loc[i, "predicted_mean"])

        output_data_dict["period"] = period_list
        output_data_dict["target"] = target_list

        return output_data_dict

    def predict_on_weeks(self, nweeks):
        output_data_dict = {}
        period_list = []
        target_list = []
        to_date = self.last_Date + pd.DateOffset(weeks=nweeks)
        self.res = self.model.get_prediction(start=pd.to_datetime(self.last_Date), end=pd.to_datetime(to_date),
                                             dynamic=False)
        df = pd.DataFrame(self.res.predicted_mean)
        df.to_csv("result.csv")
        df["date"] = pd.to_datetime(df.index)
        df["date"] = df["date"].dt.strftime("%Y-%m-%d")
        df.reset_index(inplace=True)
        for i in range(len(df)):
            period_list.append(df.loc[i, "date"])
            target_list.append(df.loc[i, "predicted_mean"])

        output_data_dict["period"] = period_list
        output_data_dict["target"] = target_list

        return output_data_dict


modelobj = Model()