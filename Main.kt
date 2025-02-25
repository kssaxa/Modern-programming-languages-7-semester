import org.knowm.xchart.*
import java.awt.Color

data class Transaction(val category: String, val amount: Double)

var transactions = mutableListOf<Transaction>()

fun insertionSort(list: MutableList<Transaction>) {
    for (i in 1 until list.size) {
        val key = list[i]
        var j = i - 1
        while (j >= 0 && list[j].amount > key.amount) {
            list[j + 1] = list[j]
            j--
        }
        list[j + 1] = key
    }
}

fun addTransaction(category: String, amount: Double) {
    transactions.add(Transaction(category, amount))
}

fun getAllTransactions(): List<Transaction> {
    return transactions
}

fun createPieChart(transactions: List<Transaction>): PieChart {
    val chart = PieChartBuilder().width(800).height(600).title("Распределение расходов").build()

    val categoryAmounts = HashMap<String, Double>()
    for (transaction in transactions) {
        categoryAmounts[transaction.category] = (categoryAmounts[transaction.category] ?: 0.0) + transaction.amount
    }

    val categories = categoryAmounts.keys.toTypedArray()
    val amounts = categoryAmounts.values.toDoubleArray()


    val amountsArray: Array<Number> = amounts.map { it as Number }.toTypedArray()


    for (i in categories.indices) {
        chart.addSeries(categories[i], amountsArray[i])
    }

    val colors = arrayOf(
        Color(255, 153, 153),
        Color(173, 216, 230),
        Color(144, 238, 144),
        Color(255, 255, 153),
        Color(200, 162, 200),
        Color(255, 204, 153)
    )

    for (i in categories.indices) {
        chart.getStyler().setSeriesColors(colors)
    }

    return chart
}

fun main() {

    println("Введите категорию и сумму транзакции или -1 для завершения")

    while (true) {
        println("Категория:")
        val category = readln()

        println("Сумма:")
        val amount = readln().toDouble()
        if (amount == -1.0) {
            break
        }

        addTransaction(category, amount)
    }

    println(getAllTransactions())
    insertionSort(transactions)

    val chart = createPieChart(transactions)
    SwingWrapper(chart).displayChart()

    /*addTransaction("Еда", 500.0)
    addTransaction("Транспорт", 200.0)
    addTransaction("Развлечения", 300.0)
    addTransaction("Покупки", 150.0)
    addTransaction("Прочее", 100.0)
    addTransaction("Еда", 150.0)
    addTransaction("Транспорт", 50.0)
   */
}
