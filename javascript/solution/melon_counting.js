
// Learning how to write scripts in javascript.

var melonsToAdd = ['Ogen', 'Horned Melon', 'Watermelon', 'Casaba',
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

// Take an array and return a map with the count for each melon.
function countMelons(melonsArray){

    let melonCounts = new Map();
    let melon;

    for (let i = 0; i < melonsArray.length; i++){
        melon = melonsArray[i];

        if (melonCounts.has(melon)){
            melonCounts.set(melon, melonCounts.get(melon) + 1);
        }
        else{
            melonCounts.set(melon, 1);
        }

    }

    return melonCounts;

}

countMelons(melonsToAdd);
