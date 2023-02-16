export default function groupByKey(key, items) {
    let keys = [];
    let groupedItems = {};
    for (let item of items) {
        let currentKey = item[key];
        if (keys.includes(currentKey)) {
            groupedItems[currentKey].push({
               ...item
            });
        } else {
            groupedItems[currentKey] = [
                {
                   ...item
                },
            ];
        }
        keys.push(currentKey);
    }
    return groupedItems;
}
