# TODO: Implement unit tests for Author model
# Testing requirements:
# # - Test the Author model's string representation.
# # - Test the Author model's name CharField max_length.
# # - Test the Author model's bio TextField optional/blank behavior.
# # - Test creating multiple Author instances and basic queries.

# TODO: Implement unit tests for Book model
# Testing requirements:
# # - Test the Book model's string representation.
# # - Test the Book model's title CharField max_length.
# # - Test the Book model's isbn unique constraint.
# # - Test the Book model's foreign key to Author (on_delete CASCADE).
# # - Test total_copies and available_copies default values and integer behavior.
# # - Test that deleting an Author cascades to related Book records.

# TODO: Implement unit tests for Member model
# Testing requirements:
# # - Test the Member model's string representation.
# # - Test the Member model's email unique constraint and EmailField validation.
# # - Test the Member model's membership_date auto_now_add behavior.
# # - Test phone field max_length and saving/retrieving members.

# TODO: Implement unit tests for BorrowRecord model
# Testing requirements:
# # - Test the BorrowRecord model's string representation.
# # - Test BorrowRecord creation links Book and Member correctly.
# # - Test borrow_date auto_now_add behavior and return_date null/blank handling.
# # - Test that deleting a Book or Member cascades to BorrowRecord.
# # - Test business logic edge case: borrowing when available_copies is zero (if enforced in future).
