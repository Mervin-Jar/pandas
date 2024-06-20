import pandas as pd

data = [[6, 'Alice'], [2, 'Bob'], [7, 'Alex']]
users = pd.DataFrame(data, columns=['user_id', 'user_name']).astype({'user_id':'Int64', 'user_name':'object'})
data = [[215, 6], [209, 2], [208, 2], [210, 6], [208, 6], [209, 7], [209, 6], [215, 7], [208, 7], [210, 2], [207, 2], [210, 7]]
register = pd.DataFrame(data, columns=['contest_id', 'user_id']).astype({'contest_id':'Int64', 'user_id':'Int64'})

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    # Calculate the total number of unique users
    total_users = users["user_id"].nunique()

    # Count the distinct user_id in each contest_id and calculate the percentage
    register_grouped = (
        register.groupby("contest_id")["user_id"]
        .nunique()
        .reset_index(name="count_unique_users")
    )

    # Calculate the percentage
    register_grouped["percentage"] = (
        register_grouped["count_unique_users"] / total_users
    ) * 100

    # Round the percentage to 2 decimal places
    register_grouped["percentage"] = register_grouped["percentage"].round(2)

    # Sort the results by percentage in descending order and then by contest_id
    register_grouped = register_grouped.sort_values(
        by=["percentage", "contest_id"], ascending=[False, True]
    )

    # Select only the contest_id and percentage columns
    final_df = register_grouped[["contest_id", "percentage"]]

    return final_df

print(users_percentage(users,register))