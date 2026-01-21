# TODO: Implement unit tests for AuthorSerializer
# Testing requirements:
# # - Test the AuthorSerializer serializes id, name, and bio.
# # - Test deserialization: creating an Author from valid payload succeeds.
# # - Test missing bio (optional) is accepted and handled.
# # - Test invalid payloads return appropriate ValidationError.

# TODO: Implement unit tests for BookSerializer
# Testing requirements:
# # - Test the BookSerializer serializes id, title, author, author_name, isbn, total_copies, available_copies.
# # - Test validate_isbn rejects non-13-character ISBNs.
# # - Test validate prevents available_copies > total_copies.
# # - Test creating/updating a Book with nested author id works.
# # - Test read-only author_name is present but cannot be written.

# TODO: Implement unit tests for MemberSerializer
# Testing requirements:
# # - Test the MemberSerializer serializes id, name, email, phone, membership_date.
# # - Test membership_date is read-only on create/update.
# # - Test email validation and unique constraint behavior (duplicate email raises error).
# # - Test deserialization with invalid email returns ValidationError.

# TODO: Implement unit tests for BorrowRecordSerializer
# Testing requirements:
# # - Test the BorrowRecordSerializer serializes book, book_title, member, member_name, borrow_date, return_date.
# # - Test write-only book_id and member_id accept ids to create BorrowRecord.
# # - Test that borrow_date is read-only and set automatically.
# # - Test serializing an active vs returned borrow shows return_date correctly.
# # - Test invalid book_id/member_id produce ValidationError.

# TODO: Integration tests for serializer + view interactions
# Testing requirements:
# # - Serialize payloads used by BookViewSet.borrow and BookViewSet.return_book actions; ensure serializers and view logic agree on field names (member_id, book_id).
# # - Test round-trip: serializer -> model save -> serializer yields expected read-only fields (e.g., book_title, author_name).
# # - Document any mismatch between view payload expectations and serializer fields.
