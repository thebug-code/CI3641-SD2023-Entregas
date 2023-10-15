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

    @Test
    fun vectorScalarMultiplication() {
        val expected = Vector(-18, 20, -5)
        assertEquals(expected, v1 % v2)
    }

    @Test
    fun vectorCrossProduct() {
        val expected = Vector(52, 27, 42)
        assertEquals(expected, v1 * v2)
    } 
    
    @Test
    fun vectorAddition2() {
        val expected = Vector(2, 3, 10)
        assertEquals(expected, v1 + 5)
    }

    @Test
    fun vectorSubtraction2() {
        val expected = Vector(-8, -7, 0)
        assertEquals(expected, v1 - 5)
    }

    @Test
    fun vectorScalarMultiplication2() {
        val expected = Vector(-15, -10, 25)
        assertEquals(expected, v1 % 5)
    }
}
