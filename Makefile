simulate: simulate.o
	$(info Linking $<)
	g++ -o $@ $@.o /usr/local/lib/libraylib.so
%.o: %.cpp
	$(info Compiling $<)
	g++ -std=c++17 -c $<
clean: 
	$(info Deleting object files and executables.)
	rm *.o simulate
	


