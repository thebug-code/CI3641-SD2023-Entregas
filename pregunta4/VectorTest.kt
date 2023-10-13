import kotlin.test.Test
import kotlin.test.assertEquals
import com.threedimvector.Vector

internal class VectorTest {

    private val v1 = Vector(-3, -2, 5)
    private val v2 = Vector(6, -10, -1)

    @Test
    fun vectorAddition() {
        val expected = Vector(3, -12, 4)
        assertEquals(expected, v1 + v2)
    }

    @Test
    fun vectorSubtraction() {
        val expected = Vector(-9, 8, 6)
        assertEquals(expected, v1 - v2)
    }
}
