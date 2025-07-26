from typing import List

from api.schemas.common import FilteringQuery, OrderingQuery, GroupingQuery


def filtering_queries_to_schemas(filtering_query_strings: List[str]) -> List[FilteringQuery]:
    return filtering_queries


def ordering_query_to_schema(ordering_query_string: str) -> OrderingQuery:
    return ordering_query


def grouping_query_to_schema(grouping_query_string: str) -> GroupingQuery:
    return grouping_query
