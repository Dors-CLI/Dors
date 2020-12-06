import pandas_datareader as data_web #pip install pandas-datareader
import matplotlib.pyplot as plt #pip install matplotlib

print("DorStock v1.0")
print("Press Control-C to quit.")
print("\n")

def get_quote():
    global company
    company = input("Enter a company ticker to get the stock for: ")
    df = data_web.DataReader((company),data_source = "yahoo")
    return df

def graph_df(df):
    plt.figure(figsize=(16, 8))
    plt.title('Close Price History For '+(company))
    plt.plot(df['Close'])
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Close Price USD ($)', fontsize=18)
    plt.show()

while True:
    try:
        graph_df(get_quote())
    except KeyboardInterrupt:
        plt.close('all')
        break
    except:
        print("An error occured.")
