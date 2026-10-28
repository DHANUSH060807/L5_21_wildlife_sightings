
"""Track wildlife sightings and summarize recorded animal counts."""

import hashlib
import sqlite3
from typing import Optional


def create_connection() -> sqlite3.Connection:
    """Create an in-memory database and its sightings table."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        """
        CREATE TABLE sightings (
            id INTEGER PRIMARY KEY,
            species TEXT NOT NULL,
            zone TEXT NOT NULL,
            count INTEGER NOT NULL
        )
        """
    )
    return connection


def log_sighting(
    connection: sqlite3.Connection,
    species: str,
    zone: str,
    count: int,
    extras: Optional[dict[str, int]] = None,
) -> dict[str, int]:
    """Record a sighting and update the species totals."""
    if not species.strip():
        raise ValueError("Species must not be empty.")
    if not zone.strip():
        raise ValueError("Zone must not be empty.")
    if not isinstance(count, int) or count < 0:
        raise ValueError("Count must be a non-negative integer.")

    connection.execute(
        """
        INSERT INTO sightings (species, zone, count)
        VALUES (?, ?, ?)
        """,
        (species, zone, count),
    )

    if extras is None:
        extras = {}

    extras[species] = extras.get(species, 0) + count
    return extras


def observer_id(observer: str) -> str:
    """Return a short identifier for an observer."""
    return hashlib.sha256(observer.encode("utf-8")).hexdigest()[:6]


def zone_summary(connection: sqlite3.Connection, zone: str) -> int:
    """Return the total animal count recorded in a zone."""
    row = connection.execute(
        "SELECT SUM(count) FROM sightings WHERE zone = ?",
        (zone,),
    ).fetchone()
    return row[0] or 0


def rarest_species(connection: sqlite3.Connection) -> Optional[str]:
    """Return the least-recorded species, or None if no data exists."""
    row = connection.execute(
        """
        SELECT species, SUM(count) AS total
        FROM sightings
        GROUP BY species
        ORDER BY total ASC, species ASC
        LIMIT 1
        """
    ).fetchone()

    if row is not None:
        return row[0]
    return None


def main() -> None:
    """Run a demonstration of the wildlife sightings tracker."""
    connection = create_connection()

    try:
        totals = log_sighting(connection, "Leopard", "North", 1)
        log_sighting(connection, "Chital", "North", 24, totals)
        log_sighting(connection, "Hornbill", "East", 3, totals)

        print(
            observer_id("Arun"),
            zone_summary(connection, "North"),
            rarest_species(connection),
        )
    finally:
        connection.close()


if __name__ == "__main__":
    main()
