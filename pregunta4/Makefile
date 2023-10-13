KC = kotlinc
KFLAG = -cp
LIB = lib
OUT_DIR = out

all: ThreeDimVectorKt.class VectorTestKt.class

ThreeDimVectorKt.class: ThreeDimVector.kt
	$(KC) $(KFLAG) . ThreeDimVector.kt -d .

VectorTestKt.class: VectorTest.kt
	$(KC) $(KFLAG) .:$(LIB)/kotlin-test-1.9.20-RC.jar:$(LIB)/kotlin-test-junit-1.9.20-RC.jar:$(LIB)/junit-4.13.2.jar VectorTest.kt -d .

clean:
	rm -rf *.class META-INF
