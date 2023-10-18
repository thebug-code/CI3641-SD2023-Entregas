
import com.programsimulator.ProgramSimulator

import org.junit.Before
import org.junit.After
import org.junit.Test
import java.io.ByteArrayInputStream
import java.io.ByteArrayOutputStream
import java.io.PrintStream
import kotlin.test.assertEquals
import kotlin.test.assertTrue


internal class ProgramTest {
    private val originalInput = System.`in`
    private val originalOutput = System.out

    private val program = ProgramSimulator()

    private val testInput = ByteArrayInputStream("DEFINIR\nSALIR".toByteArray())
    private val testOutput = ByteArrayOutputStream()

    @Before
    fun setUp() {
        System.setOut(PrintStream(testOutput))
    }

    @After
    fun tearDown() {
        System.setIn(originalInput)
        System.setOut(originalOutput)
    }

    @Test
    fun testRun() {
        val customInput = ByteArrayInputStream("DEFINIR\nSALIR".toByteArray())
        System.setIn(customInput)
        program.run()
        val output = testOutput.toString().trim() // Captura la salida para su posterior evaluación
        assertEquals(">$ Error: número de parámetros incorrecto\n>$", output)
    }

    @Test
    fun testRun2() {
        val customInput = ByteArrayInputStream("DEFINIR PROGRAMA\nSALIR".toByteArray())
        System.setIn(customInput)
        program.run()
        val output = testOutput.toString().trim() // Captura la salida para su posterior evaluación
        assertEquals(">$ Error: número de parámetros incorrecto\n>$", output)
    }

    @Test
    fun testRun3() {
        val customInput = ByteArrayInputStream("DEFINIR PROGRAMA factorial\nSALIR".toByteArray())
        System.setIn(customInput)
        program.run()
        val output = testOutput.toString().trim() // Captura la salida para su posterior evaluación
        assertEquals(">$ Error: número de parámetros incorrecto\n>$", output)
    }

    @Test
    fun testRun4() {
        val customInput = ByteArrayInputStream("DEFINIR PROGRAMA factorial ?\nSALIR".toByteArray())
        System.setIn(customInput)
        program.run()
        val output = testOutput.toString().trim() // Captura la salida para su posterior evaluación
        assertEquals(">$ Error: el nombre del lenguaje '?' no es alfanumérico\n>$", output)
    }

    @Test
    fun testRun5() {
        val customInput = ByteArrayInputStream("DEFINIR PROGRAMA factorial Java\nDEFINIR PROGRAMA factorial C\nSALIR".toByteArray())
        System.setIn(customInput)
        program.run()
        val output = testOutput.toString().trim()
        assertEquals(">$ Se definió el programa 'FACTORIAL', ejecutable en 'JAVA'\n>$ Error: el programa 'FACTORIAL' ya está definido\n>$", output)
    }

    @Test
    fun testRun6() {
        val customInput = ByteArrayInputStream("DEFINIR PROGRAMA fibonacci LOCAL\nEJECUTABLE fibonacci\nDEFINIR PROGRAMA factorial Java\nEJECUTABLE factorial\nDEFINIR INTERPRETE C Java\nDEFINIR TRADUCTOR C Java C\nEJECUTABLE factorial\nDEFINIR INTERPRETE LOCAL C\nEJECUTABLE factorial\nDEFINIR PROGRAMA holamundo Python3\nDEFINIR TRADUCTOR wtf42 Python3 LOCAL\nEJECUTABLE holamundo\nDEFINIR TRADUCTOR C wtf42 Java\nEJECUTABLE holamundo\nSALIR".toByteArray())
        System.setIn(customInput)
        program.run()
        val output = testOutput.toString().trim()

        assertEquals(">$ Se definió el programa 'FIBONACCI', ejecutable en 'LOCAL'\n>$ Si, es posible ejecutar el programa 'FIBONACCI'\n>$ Se definió el programa 'FACTORIAL', ejecutable en 'JAVA'\n>$ No es posible ejecutar el programa 'FACTORIAL'\n>$ Se definió un intérprete para 'JAVA', escrito en 'C'\n>$ Se definió un traductor de 'JAVA' hacia 'C', escrito en 'C'\n>$ No es posible ejecutar el programa 'FACTORIAL'\n>$ Se definió un intérprete para 'C', escrito en 'LOCAL'\n>$ Si, es posible ejecutar el programa 'FACTORIAL'\n>$ Se definió el programa 'HOLAMUNDO', ejecutable en 'PYTHON3'\n>$ Se definió un traductor de 'PYTHON3' hacia 'LOCAL', escrito en 'WTF42'\n>$ No es posible ejecutar el programa 'HOLAMUNDO'\n>$ Se definió un traductor de 'WTF42' hacia 'JAVA', escrito en 'C'\n>$ Si, es posible ejecutar el programa 'HOLAMUNDO'\n>$", output)
    }

    @Test
    fun testRun7() {
        val custonInput = ByteArrayInputStream("efe\nSALIR".toByteArray())
        System.setIn(custonInput)
        program.run()
        val output = testOutput.toString().trim()
        assertEquals(">$ Error: opción no válida\n>$", output)
    }

    @Test
    fun testRun8() {
        val custonInput = ByteArrayInputStream("DEFINIR TRADUCTOR C* JAVA LOCAL\nSALIR".toByteArray())
        System.setIn(custonInput)
        program.run()
        val output = testOutput.toString().trim()
        assertEquals(">$ Error: el nombre del lenguaje base 'C*' no es alfanumérico\n>$", output)
    }

    @Test
    fun testRun9() {
        val custonInput = ByteArrayInputStream("DEFINIR TRADUCTOR C JAVA+ LOCAL\nSALIR".toByteArray())
        System.setIn(custonInput)
        program.run()
        val output = testOutput.toString().trim()
        assertEquals(">$ Error: el nombre del lenguaje origen 'JAVA+' no es alfanumérico\n>$", output)
    }

    @Test
    fun testRun10() {
        val custonInput = ByteArrayInputStream("DEFINIR TRADUCTOR C JAVA LOC)AL\nSALIR".toByteArray())
        System.setIn(custonInput)
        program.run()
        val output = testOutput.toString().trim()
        assertEquals(">$ Error: el nombre del lenguaje destino 'LOC)AL' no es alfanumérico\n>$", output)
    }

    @Test
    fun testRun11() {
        val custonInput = ByteArrayInputStream("DEFINIR TRADUCTOR C* JAVA\nSALIR".toByteArray())
        System.setIn(custonInput)
        program.run()
        val output = testOutput.toString().trim()
        assertEquals(">$ Error: número de parámetros incorrecto\n>$", output)
    }
}

