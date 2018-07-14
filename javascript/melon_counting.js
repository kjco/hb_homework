// Our customers are going to buy lots of melons!

const melons_to_add = ['Ogen', 'Horned Melon', 'Watermelon', 'Casaba',
                 'Sharlyn', 'Xigua', 'Ogen', 'Christmas', 'Christmas',
                 'Christmas', 'Christmas', 'Watermelon', 'Sharlyn', 'Xigua',
                 'Cantaloupe', 'Christmas', 'Watermelon', 'Christmas',
                 'Sharlyn', 'Christmas', 'Cantaloupe', 'Casaba', 'Cantaloupe',
                 'Santa Claus', 'Horned Melon', 'Watermelon', 'Ogen',
                 'Horned Melon', 'Cantaloupe', 'Xigua', 'Horned Melon', 'Sharlyn',
                 'Horned Melon', 'Sharlyn', 'Cantaloupe', 'Christmas',
                 'Horned Melon', 'Horned Melon', 'Horned Melon', 'Xigua', 'Xigua',
                 'Watermelon', 'Cantaloupe', 'Casaba', 'Cantaloupe', 'Casaba',
                 'Watermelon', 'Santa Claus', 'Casaba'];

// console.log(melons_to_add);

function countMelons(melonLst) {

    let melon_counts = new Map();

    for (let melon of melonLst) {
        // console.log(melon);
        if (melon_counts.has(melon)) {
            melon_counts.set(melon, (melon_counts.get(melon)+1));
        }
        else {
            melon_counts.set(melon, 1);
        }
    }
    return melon_counts;
}

countMelons(melons_to_add);