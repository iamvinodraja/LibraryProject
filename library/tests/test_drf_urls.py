# TODO: Implement unit tests for urls.py
# Testing requirements:
# # - Verify the router registers the top-level endpoints: authors, books, members, borrows.
# # - Assert that the base include (empty path) exposes the router URLs.
# # - Test that list (GET) and retrieve (GET /{id}/) endpoints exist for each registered viewset.
# # - Test that unsupported HTTP methods on endpoints return 405 Method Not Allowed.

# TODO: Implement unit tests for Book custom actions in routes 
# Testing requirements:
# # - Test GET /books/available/ returns 200 and is routable.
# # - Test POST /books/{id}/borrow/ is routable and accepts member_id in payload.
# # - Test POST /books/{id}/return_book/ is routable and accepts member_id in payload.

# TODO: Implement unit tests for Member and BorrowRecord custom routes
# Testing requirements:
# # - Test GET /members/{id}/borrowed_books/ is routable and returns 200 for existing member.
# # - Test GET /borrows/active/ is routable and returns 200.
# # - Test route reverse lookups (using reverse('...')) resolve to correct paths where applicable.

# TODO: Integration tests for URL -> view behavior
# Testing requirements:
# # - End-to-end: call POST /books/{id}/borrow/ and verify the view, serializer, and model side-effects occur.
# # - End-to-end: call POST /books/{id}/return_book/ and verify side-effects.
# # - Verify error routes: POST /books/{id}/borrow/ with missing/invalid member_id yields 400/404 as implemented.
