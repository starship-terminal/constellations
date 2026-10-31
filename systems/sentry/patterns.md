# Sentry patterns

## Navigation and data scope

The global rail and section sidebar preserve location while project, environment, date and query controls scope the main data area. [Issue empty state](screenshots/app/issues-dark-empty.png).

## Query building

The query menu groups fields by type and keeps a help panel beside suggestions. The focused input has a visible purple ring. [Search](screenshots/app/issues-dark-search.png).

## Trace exploration

A query/aggregation panel sits beside a chart and sample table. Selecting a span opens a waterfall with a neighbouring attributes panel. [Explorer](screenshots/app/traces-light-list.png), [waterfall](screenshots/app/trace-light-waterfall.png).

## Empty and loading

The issue list explains how filters can produce no matches. A span disclosure shows a spinner while attributes load. [Empty](screenshots/app/issues-light-empty.png), [loading](screenshots/app/traces-dark-span-loading.png).

## Dialogs

Command search appears over a dimmed page; feedback uses a lower-right form with a textarea and explicit Cancel. Nothing was submitted. [Commands](screenshots/app/command-light-dialog.png), [feedback](screenshots/app/feedback-light-dialog.png).
