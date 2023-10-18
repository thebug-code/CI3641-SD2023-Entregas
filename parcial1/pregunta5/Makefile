KC = kotlinc
KFLAG = -cp
LIB_DIR = lib
OUT_DIR = out

# Lista de archivos .jar en el directorio "lib"
JARS := $(wildcard $(LIB_DIR)/*.jar)

# Agrega los archivos .jar al classpath
CLASSPATH := $(shell echo $(JARS) | sed 's/ /:/g')

all: ProgramSimulatorKt.class ProgramTestKt.class

ProgramSimulatorKt.class: ProgramSimulator.kt
	$(KC) $(KFLAG) .:"$(CLASSPATH)" -d . $^

ProgramTestKt.class: ProgramTest.kt
	$(KC) $(KFLAG) .:"$(CLASSPATH)" -d . $^

clean:
	rm -rf *.class *.exec META-INF com coverage-report

.PHONY: all clean
