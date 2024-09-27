import pandas as pd


def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult.data.csv')

    race_count = pd.Series(df['race'].value_counts())

    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    numero_bachelors = df[df['education']=='Bachelors'].shape[0]
    numero_total = df.shape[0]

    percentage_bachelors = round((df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1)

    df_higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    num_higher_education_rich = df_higher_education[df_higher_education['salary'] == '>50K'].shape[0]

    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].shape[0]

    df_lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    num_lower_education_rich = df_lower_education[df_lower_education['salary'] == '>50K'].shape[0]

    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].shape[0]

    numero_total = df.shape[0]

    higher_education_rich = round((num_higher_education_rich / higher_education) * 100, 1)
    lower_education_rich = round((num_lower_education_rich / lower_education) * 100, 1)

    min_work_hours = df['hours-per-week'].min()

    num_min_workers = df[df['hours-per-week'] == 1]
    num_num_min_workers = num_min_workers.shape[0]
    num_min_workers_50k = num_min_workers[num_min_workers['salary']== '>50K'].shape[0]

    rich_percentage = (num_min_workers_50k/num_num_min_workers)*100

    valores_50k = df[df['salary'] == '>50K']
    paises_valores_50k = valores_50k['native-country']
    pessoas_50k = paises_valores_50k.value_counts()

    pessoas_pais = df['native-country'].value_counts()

    porcentagem = (pessoas_50k/pessoas_pais)*100
    highest_earning_country_percentage = round(porcentagem.max(), 1)

    highest_earning_country = porcentagem.idxmax()

    india_valores_50k = valores_50k[valores_50k['native-country']=='India']
    ocupacao_india_50k = india_valores_50k['occupation'].value_counts()
    top_IN_occupation = ocupacao_india_50k.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
