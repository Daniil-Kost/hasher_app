categories = [
    {
        "title": "Food",
        "subcategories": [
            {"title": "Bread"},
            {
                "title": "Meat",
                "subcategories": [
                    {"title": "Pork",
                     "subcategories": [
                         {"title": "White pork", 
                          "subcategories": [
                             {"title": "French white pork"},
                             {"title": "Italian white pork"},
                         ]},
                        {"title": "Black pork"},
                     ]},
                    {"title": "Beef"},
                ],
            },
            {"title": "Cheese"},
        ],
    },
    {"title": "Drinks"},
]

# Food
# -Bread
# -Meat
# --Pork
# ---White pork
# ----French white pork
# ----Italian white pork
# ---Black pork
# --Beef
# -Cheese
# Drinks


def get_subcategories(subcategories, line="-"):
    if subcategories:
        help_line = line
        for subcategorie in subcategories:
            print(line + subcategorie.get("title"))
            if subcategorie.get("subcategories"):
                line += "-"
                get_subcategories(subcategorie.get("subcategories"), line)
                line = help_line


def main(category):
    my_dict = category
    title_my_dict = my_dict.get("title")
    print(title_my_dict)
    subcategories = my_dict.get("subcategories")
    if subcategories:
        get_subcategories(subcategories)


for category in categories:
    main(category)

