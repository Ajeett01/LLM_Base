CREATE TABLE trees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    species VARCHAR(100),
    location VARCHAR(200),
    diameter_inches DECIMAL(5,2),
    height_feet INTEGER,
    planting_date DATE,
    health_condition VARCHAR(50)
);

-- Insert sample data
INSERT INTO trees (species, location, diameter_inches, height_feet, planting_date, health_condition) VALUES
    ('Norway Maple', '123 Main St', 24.5, 45, '2000-03-15', 'Good'),
    ('Red Oak', '456 Elm St', 36.0, 60, '1995-04-20', 'Excellent'),
    ('Silver Birch', '789 Oak Ave', 18.3, 35, '2010-05-10', 'Fair'),
    ('American Elm', '321 Pine Rd', 42.1, 55, '1990-06-25', 'Good'),
    ('Japanese Cherry', '654 Maple Dr', 12.7, 20, '2015-04-01', 'Excellent'),
    ('London Plane', '987 Cedar Ln', 30.2, 50, '2005-03-30', 'Good'),
    ('Honey Locust', '147 Birch Blvd', 15.8, 30, '2012-09-15', 'Fair'),
    ('Pin Oak', '258 Spruce Way', 28.4, 48, '2003-10-20', 'Good'),
    ('Green Ash', '369 Willow St', 22.6, 40, '2008-05-05', 'Poor'),
    ('Sugar Maple', '741 Aspen Ct', 33.9, 52, '1998-04-12', 'Good');
