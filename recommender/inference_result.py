def display_inference_result(inference_result_df, customer_id, inference_type):
    inference_result_df = inference_result_df.rename(
        columns={"user_id": "CustomerID", "item_id": "StockCode", "score": "Recommendation Score"}
    )
    inference_result_df["StockCode"] = inference_result_df.StockCode.astype(str)
    stock_code_desc = stock_code_desc_look_up.groupby(["StockCode"]).agg(lambda x: x.iloc[0])[
        ["Description"]
    ]
    inference_result_df = inference_result_df.join(stock_code_desc, on="StockCode")
    inference_result_df = inference_result_df[
        ["CustomerID", "StockCode", "Description", "Recommendation Score"]
    ]

    if inference_type == "batch":
        inference_result_df = inference_result_df.loc[
            inference_result_df["CustomerID"] == customer_id
        ]
        display(
            md(
                "**[ <u>Batch Transform</u> ] Recommended Items with the Ranking for a Customer ID : {}**".format(
                    customer_id
                )
            )
        )
    elif inference_type == "realtime":
        display(
            md(
                "**[ <u>Real-Time Inference</u> ] Recommended Items with the Ranking for a Customer ID : {}**".format(
                    customer_id
                )
            )
        )
    return display(inference_result_df.style.hide_index())