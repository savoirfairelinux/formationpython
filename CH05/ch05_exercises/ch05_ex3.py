class Snake:
    internal_array = [];
    
    def len(self):
        return len(self.internal_array)
    
    def top(self):
        if len(self.internal_array) > 0 :
            return self.internal_array[-1]
        return None;

    def pop(self):
        if self.len() > 1 :
            return_value = self.internal_array[-1]
            self.internal_array = self.internal_array[0:-1];
            return return_value;
        return None;
    
    def push(self, value):
        self.internal_array.append(value);