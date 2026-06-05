def Strongest_Extension(class_name, extensions):
    def calculate_strength(ext):
        uppercase = sum(1 for c in ext if c.isupper())
        lowercase = sum(1 for c in ext if c.islower())
        return uppercase - lowercase
    
    strongest = max(extensions, key=calculate_strength)
    return f"{class_name}.{strongest}"
