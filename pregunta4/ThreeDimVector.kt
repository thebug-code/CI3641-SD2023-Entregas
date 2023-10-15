/**
 * Definicion de vectores de tres coordenadas y de las operaciones suma, resta, 
 * productor cruz, producto punto y norma sobre estos.
 */
package com.threedimvector

data class Vector(val x: Int, val y: Int, val z: Int) {
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
    
    operator fun plus(n: Int): Vector {
        return Vector(x + n, y + n, z + n)
    }
    
    operator fun minus(n: Int): Vector {
        return Vector(x - n, y - n, z - n)
    }
    
    operator fun rem(n: Int): Vector {
        return Vector(x * n, y * n, z * n)
    }

    override fun equals(other: Any?): Boolean {
        when(other) {
    	    is Vector -> {
                return x == other.x && y == other.y && z == other.z
            } else -> return false
    	}
    }
}
