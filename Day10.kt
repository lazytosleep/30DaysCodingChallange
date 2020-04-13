/*
Prob: MinStack
Impl Min Stack with APIs getMin, push, pop in constant time
Idea is to maintian a seperate min stack along with regular stack
Min stack should have min or equal to min element pushed
 */
class MinStack {

    private val stack: MutableList<Int> = mutableListOf()
    private val minStack: MutableList<Int> = mutableListOf()

    fun push(x: Int) {
        stack.add(x)
        if (minStack.size == 0 || x <= getMin()) {
            minStack.add(x)
        }
    }

    fun pop() {
        if(stack.count() >= 0) {
            val ele = stack.last()
            stack.removeAt(stack.size - 1)
            if (ele == getMin()) {
                minStack.removeAt(minStack.size -1)
            }
        }
    }

    fun top(): Int {
        return stack.last()
    }

    fun getMin(): Int {
        return minStack.last()
    }

}

fun main() {
    val stack = MinStack()
    stack.push(-2)
    stack.push(-3)
    print(stack.getMin())
    stack.pop()
    print(stack.top())
}


