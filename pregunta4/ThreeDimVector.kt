/**
 * Definicion de vectores de tres coordenadas y de las operaciones suma, resta, 
 * productor cruz, producto punto y norma sobre estos.
 */

package com.threedimvector
import kotlin.math.sqrt
import java.text.DecimalFormat

data class Vector(val x: Double, val y: Double, val z: Double) {
    private val df = DecimalFormat("#.##")

    operator fun plus(other: Vector): Vector {
        return Vector(x + other.x, y + other.y, z + other.z)
    }
    
    operator fun minus(other: Vector): Vector {
        return Vector(x - other.x, y - other.y, z - other.z)
    }
     
    operator fun times(other: Vector): Vector {
        return Vector(y * other.z - z * other.y, z * other.x - x * other.z, x * other.y - y * other.x)
    }
    
    operator fun rem(other: Vector): Vector {
        return Vector(x * other.x, y * other.y, z * other.z)
    }

    val norm: Double
        get() = df.format(sqrt(x * x + y * y + z * z)).toDouble()

    operator fun plus(n: Int): Vector {
        return Vector(x + n, y + n, z + n)
    }
    
    operator fun minus(n: Int): Vector {
        return Vector(x - n, y - n, z - n)
    }
    
    operator fun rem(n: Int): Vector {
        return Vector(x * n, y * n, z * n)
    }

    operator fun plus(n: Double): Vector {
        return Vector(df.format(x + n).toDouble(), df.format(y + n).toDouble(), df.format(z + n).toDouble())
    }

    operator fun minus(n: Double): Vector {
        return Vector(df.format(x - n).toDouble(), df.format(y - n).toDouble(), df.format(z - n).toDouble())
    }

    operator fun rem(n: Double): Vector {
        return Vector(df.format(x * n).toDouble(), df.format(y * n).toDouble(), df.format(z * n).toDouble())
    }
    
    override fun equals(other: Any?): Boolean {
        when(other) {
    	    is Vector -> {
                return x == other.x && y == other.y && z == other.z
            } else -> return false
    	}
    }

    companion object {
        operator fun invoke(x: Int, y: Int, z: Int): Vector {
            return Vector(x.toDouble(), y.toDouble(), z.toDouble())
        }
    }
}
