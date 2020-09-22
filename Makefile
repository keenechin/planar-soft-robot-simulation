SRC_PATH = src
BUILD_PATH = build
all: render_simulation simulate

render_simulation: $(BUILD_PATH)/render_simulation.o
	$(info Linking $<)
	g++ -o $@ $(BUILD_PATH)/$@.o /usr/local/lib/libraylib.so
simulate: $(BUILD_PATH)/simulate.o
	$(info Linking $<)
	g++ -o $@ $(BUILD_PATH)/$@.o /usr/local/lib/libraylib.so
$(BUILD_PATH)/%.o: $(SRC_PATH)/%.cpp
	$(info Compiling $^ into $@)
	g++ -std=c++17 -c $^ -o $@
clean: 
	$(info Deleting object files and executables.)
	rm  build/* simulate render_simulation
	


